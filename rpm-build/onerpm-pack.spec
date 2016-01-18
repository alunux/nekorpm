Name: onerpm-pack
Version: 1.2
Release: 1
URL: https://wonderneko.wordpress.com/
License: GPL
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-root
Requires: bash >= 4.0
Requires: dnf >= 1.0.2
Requires: dnf-plugins-core
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
mkdir -p ${RPM_BUILD_ROOT}/usr/share/onerpm-pack
install -m 755 onerpm-pack ${RPM_BUILD_ROOT}%{_bindir}
install -m 644 f23-mini-x86 ${RPM_BUILD_ROOT}%{_datadir}/onerpm-pack
install -m 644 f23-mini-x86-64 ${RPM_BUILD_ROOT}%{_datadir}/onerpm-pack

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/onerpm-pack
%attr(644,root,root) %{_datadir}/onerpm-pack/f23-mini-x86
%attr(644,root,root) %{_datadir}/onerpm-pack/f23-mini-x86-64

%changelog
* Mon Jan 18 2016 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 1.2-1
- onerpm-pack 1.2 release
- Add Fedora 23 i686 and x86_64 build environment for onerpm packaging
- Backup features
- Fix rpm missed query
- Locate backup's location with zenity or kdialog
* Sun Nov 15 2015 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 1.1-1
- onerpm-pack 1.1 release
- Add build environment for onerpm packaging
* Wed Aug 19 2015 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 1.0-1
- onerpm-pack 1.0 release
