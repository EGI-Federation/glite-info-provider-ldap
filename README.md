# glite-info-provider-ldap

Documentation is available in the `doc` directory.

## Installing from source

```sh
make install
```

## Building packages

### Building a RPM

The required build dependencies are:

- rpm-build
- make
- rsync

```sh
# Checkout tag to be packaged
git clone https://github.com/EGI-Federation/glite-info-provider-ldap.git
cd glite-info-provider-ldap
git checkout X.X.X
# Building in a container
docker run --rm -v $(pwd):/source -it centos:7
yum install -y rpm-build make rsync
cd /source && make rpm
```

The RPM will be available into the `build/RPMS` directory.

### Building a deb

```sh
# Checkout tag to be packaged
git clone https://github.com/EGI-Federation/glite-info-provider-ldap.git
cd glite-info-provider-ldap
git checkout X.X.X
# Building in a container using the source files
docker run --rm -v $(pwd):/source -it ubuntu:xenial
apt update
apt install -y devscripts debhelper make rsync python-all-dev
cd /source && make deb
```

The DEB will be available into the `build/` directory.

## Preparing a release

- Prepare a changelog from the last version, including contributors' names
- Prepare a PR with
  - Updating version and changelog in `glite-info-provider-ldap.spec`
  - Updating version and changelog in `debian/changelog`
  - Updating authors in `AUTHORS`
- Once the PR has been merged tag and release a new version in GitHub
  - Packages will be built using GitHub Actions and attached to the release page

## History

This work started under the EGEE project, and was hosted and maintained for a
long time by CERN. This is now hosted here on GitHub, maintained by the BDII
community with support of members of the EGI Federation.
