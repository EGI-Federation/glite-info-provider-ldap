NAME=$(shell grep Name: *.spec | sed 's/^[^:]*:[^a-zA-Z]*//')
VERSION=$(shell grep Version: *.spec | sed 's/^[^:]*:[^0-9]*//')
RELEASE=$(shell grep Release: *.spec | cut -d"%" -f1 | sed 's/^[^:]*:[^0-9]*//')
build=$(shell pwd)/build
dist=$(shell rpm --eval '%dist')

default:
	@echo "Nothing to do"

test:
	./test/run-tests

install:
	@echo installing ...
	@mkdir -p $(prefix)/usr/libexec/
	@mkdir -p $(prefix)/var/lib/bdii/gip/tmp/gip/
	@mkdir -p $(prefix)/var/lib/bdii/gip/tmp/gip/log/
	@mkdir -p $(prefix)/var/lib/bdii/gip/cache/gip/
	@install -m 0755 src/$(NAME) $(prefix)/usr/libexec
	@mkdir -p $(prefix)/usr/share/doc/$(NAME)-$(VERSION)
	@mkdir -p $(prefix)/usr/share/licenses/$(NAME)-$(VERSION)
	@install -m 0644 README.md $(prefix)/usr/share/doc/$(NAME)-$(VERSION)/
	@install -m 0644 AUTHORS.md $(prefix)/usr/share/doc/$(NAME)-$(VERSION)/
	@install -m 0644 COPYRIGHT $(prefix)/usr/share/licenses/$(NAME)-$(VERSION)/
	@install -m 0644 LICENSE.txt $(prefix)/usr/share/licenses/$(NAME)-$(VERSION)/

dist:
	@mkdir -p $(build)/$(NAME)-$(VERSION)/
	rsync -HaS --exclude ".git" --exclude "$(build)" * $(build)/$(NAME)-$(VERSION)/
	cd $(build); tar --gzip -cf $(NAME)-$(VERSION).tar.gz $(NAME)-$(VERSION)/; cd -

sources: dist
	cp $(build)/$(NAME)-$(VERSION).tar.gz .

prepare: dist
	@mkdir -p $(build)/RPMS/noarch
	@mkdir -p $(build)/SRPMS/
	@mkdir -p $(build)/SPECS/
	@mkdir -p $(build)/SOURCES/
	@mkdir -p $(build)/BUILD/
	cp $(build)/$(NAME)-$(VERSION).tar.gz $(build)/SOURCES
	cp $(NAME).spec $(build)/SPECS

srpm: prepare
	rpmbuild -bs --define="dist $(dist)" --define="_topdir $(build)" $(build)/SPECS/$(NAME).spec

rpm: srpm
	rpmbuild --rebuild --define="dist $(dist)" --define="_topdir $(build)" $(build)/SRPMS/$(NAME)-$(VERSION)-$(RELEASE)$(dist).src.rpm

deb: dist
	cd $(build)/$(NAME)-$(VERSION); dpkg-buildpackage -us -uc; cd -

clean:
	@rm -f *~ bin/*~ etc/*~ data/*~
	@rm -rf build dist MANIFEST
	rm -f *~ $(NAME)-$(VERSION).tar.gz

.PHONY: dist srpm rpm sources deb test clean
