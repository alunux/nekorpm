Name: nekorpm-pack
Version: 1.3
Release: 1
URL: https://wonderneko.wordpress.com/
License: GPL
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-root
Requires: bash
Requires: tar
Requires: dnf >= 1.0.2
Requires: dnf-plugins-core
Requires: createrepo_c
Requires: nekorpm
Source0: nekorpm-pack-%{version}.tar.xz
BuildArch: noarch
Summary: nekorpm-pack is a packager for .nekorpm package

%description
nekorpm-pack is a packager for .nekorpm package

%prep
%setup -q

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
mkdir -p ${RPM_BUILD_ROOT}/usr/share/%{name}/f23-{i686,x86_64}/var/lib/rpm

ls *.tar.xz | xargs -n1 tar -xf
install -m 755 %{name} ${RPM_BUILD_ROOT}%{_bindir}
install -m 644 f23-i686/var/lib/rpm/* \
        ${RPM_BUILD_ROOT}%{_datadir}/%{name}/f23-i686/var/lib/rpm
install -m 644 f23-x86_64/var/lib/rpm/* \
        ${RPM_BUILD_ROOT}%{_datadir}/%{name}/f23-x86_64/var/lib/rpm

%clean
rm -rf ${RPM_BUILD_ROOT}

%postun
rm -rf %dir %{_datadir}/%{name}/

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%attr(644,root,root) %{_datadir}/%{name}/f23-i686/var/lib/rpm/*
%attr(644,root,root) %{_datadir}/%{name}/f23-x86_64/var/lib/rpm/*

%changelog
* Sun May 22 2016 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 1.3-1
- Using rpmbd instead full root environment
- Cleanup code
* Mon Jan 18 2016 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 1.2-1
- nekorpm-pack 1.2 release
- Add Fedora 23 i686 and x86_64 build environment for nekorpm packaging
- Backup features
- Fix rpm missed query
- Locate backup's location with zenity or kdialog
* Sun Nov 15 2015 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 1.1-1
- nekorpm-pack 1.1 release
- Add build environment for nekorpm packaging
* Wed Aug 19 2015 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 1.0-1
- nekorpm-pack 1.0 release
