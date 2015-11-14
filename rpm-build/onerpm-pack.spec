Name: onerpm-pack
Version: 1.1
Release: 1
URL: https://wonderneko.wordpress.com/
License: GPL
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-root
Requires: bash >= 4.0
Requires: dnf >= 1.0.2
Requires: dnf-conf >= 1.0.2
Requires: dnf-plugins-core
Requires: dnf-yum >= 1.0.2
Source0: onerpm-pack-%{version}.tar.gz
BuildArch: noarch
Summary: onerpm-pack is a packager for .onerpm package

%description
onerpm-pack is a packager for .onerpm package

%prep
%setup

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
install -m 755 onerpm-pack ${RPM_BUILD_ROOT}%{_bindir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/onerpm-pack

%changelog
* Sun Nov 15 2015 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 1.1-1
- onerpm-pack 1.1 release
- Add build environment for onerpm packaging
* Wed Aug 19 2015 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 1.0-1
- onerpm-pack 1.0 release
