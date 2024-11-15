Name:          glite-info-provider-ldap
Version:       1.6.1
Release:       1%{?dist}
Summary:       LDAP information provider
Group:         Development/Libraries
License:       ASL 2.0
URL:           https://github.com/EGI-Federation/glite-info-provider-ldap
Source:        %{name}-%{version}.tar.gz
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
BuildRequires: rsync
BuildRequires: make
Requires:      openldap-servers
Requires: perl-File-Copy
Requires: perl-libwww-perl

%description
Information provider to query LDAP sources and return the result.

%prep
%setup -q

%build
# Nothing to build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/libexec/glite-info-provider-ldap
%attr(-, ldap, ldap) %{_sharedstatedir}/bdii/gip/tmp/gip/
%attr(-, ldap, ldap) %{_sharedstatedir}/bdii/gip/tmp/gip/log/
%attr(-, ldap, ldap) %{_sharedstatedir}/bdii/gip/cache/gip/
%doc %{_docdir}/%{name}-%{version}/README.md
%doc %{_docdir}/%{name}-%{version}/AUTHORS.md
%license /usr/share/licenses/%{name}-%{version}/COPYRIGHT
%license /usr/share/licenses/%{name}-%{version}/LICENSE.txt

%changelog
* tue Nov 15 2024 baptiste grenier <baptiste.grenier@egi.eu> - 1.7.1-1
- Drop support for RHEL7. (#21) (baptiste grenier)

* tue Nov 15 2024 baptiste grenier <baptiste.grenier@egi.eu> - 1.6.2-1
- Add missing perl dependencies for el8. (#21) (baptiste grenier)

* tue Apr 28 2024 baptiste grenier <baptiste.grenier@egi.eu> - 1.6.1-1
- Add missing perl dependencies for el9. (#16) (baptiste grenier)

* Tue Apr 4 2023 Baptiste Grenier <baptiste.grenier@egi.eu> - 1.6.0-1
- Build and release using CentOS 7, AlmaLinux 8 and 9. (#12) (Baptiste Grenier)
- Sync repo with other bdii-related ones. (#12) (Baptiste Grenier)

* Wed Sep 7 2022 Baptiste Grenier <baptiste.grenier@egi.eu> - 1.5.0-1
- Suppress the software and job information (#2) (Laurence Field)
- Use GitHub Actions to lint, build, and upload packages to GitHub (#5) (Baptiste Grenier)

* Fri Sep 27 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.4.8-1
- BUG #102675: Increase the default max size of LDIF files to 25MB
- BUG #102698: Start with a clean cache directory in the case of Top BDIIs

* Thu Sep 26 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.4.7-1
- BUG #102608: Remove completely top level BDII cache
- BUG #102675: Increase the size of queried LDIF files
- Log in a summary of the total number of failed LDAP URLs

* Wed Sep 04 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.4.6-1
- BUG #102384: rollback ldap query to the site BDII and remove change for ARC integration

* Mon Jul 29 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.4.5-1
- Removed log messages used for debugging and added missing state attributes
- Removed cache for Top BDII and define it only for site BDII
- Fixed missing ";"
- BUG #101805: Set to 'unknown' cached GLUE 2 state attributes

* Wed Apr 24 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.4.4-2
- Added Source URL information

* Tue Dec 04 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.4.4-1
- Fix after testing: Use 'resource' instead of 'services' since new alias is not valid in previous BDII versions.

* Tue Nov 20 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.4.3-1
- BUG #98848: Accept GLUE 2.0 LDAP URLs
- BUG #95681: ARC tree in BDII

* Wed Oct 24 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.4.2-1
- BUG #97395: Fixed rpmlint errors: Changed glite-info-provider-ldap path from /opt/glite to /usr
- Added a README file

* Mon Jun 06 2011 Laurence Field <laurence.field@cern.ch> - 1.4.1-1
- Fix for bug #81637 (Missing dependency)

* Tue Mar 22 2011 Laurence Field <laurence.field@cern.ch> - 1.4.0-1
- Change the location of the var directory

* Fri Mar 4 2011 Laurence Field <laurence.field@cern.ch> - 1.3.5-1
- Implemented IS-220

* Fri Feb 18 2011 Laurence Field <laurence.field@cern.ch> - 1.3.4-1
- Implemented IS-207

* Mon Feb 14 2011 Laurence Field <laurence.field@cern.ch> - 1.3.3-1
- Fixed bug 78067

* Thu Apr 1 2010 Laurence Field <laurence.field@cern.ch> - 1.3.0-1
- New version that can also obtain Glue 2.0 information
