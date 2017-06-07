# glite-info-provider-ldap

Documentation is available in the `doc` directory.

## Installing from source

```sh
make install
```

## Building packages

* It is possible to easily build pacakges for Ubuntu and CentOS using
  the provided `Makefile-build-docker` makefile leveraging the use of
  docker containers.

```sh
# Building an Ubuntu Xenial deb
make -f Makefile-build-docker deb
# Building a CentOS 7 RPM
make -f Makefile-build-docker rpm
```

