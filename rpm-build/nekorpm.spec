Name: nekorpm
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
Source0: nekorpm-%{version}.tar.xz
BuildArch: noarch
Summary: nekorpm is a single offline installer for Fedora

%description
nekorpm is a single offline installer for Fedora.

%prep
%setup -q

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
mkdir -p ${RPM_BUILD_ROOT}/usr/share/nekorpm/functions/
mkdir -p ${RPM_BUILD_ROOT}/usr/share/nekorpm/RPM-GPG-KEY/

install -m 755 nekorpm ${RPM_BUILD_ROOT}%{_bindir}
install -m 644 functions/* ${RPM_BUILD_ROOT}%{_datadir}/nekorpm/functions
install -m 644 RPM-GPG-KEY/* ${RPM_BUILD_ROOT}%{_datadir}/nekorpm/RPM-GPG-KEY/

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/nekorpm
%dir %{_datadir}/nekorpm
%dir %{_datadir}/nekorpm/functions
%dir %{_datadir}/nekorpm/RPM-GPG-KEY
%attr(644,root,root) %{_datadir}/nekorpm/functions/*
%attr(644,root,root) %{_datadir}/nekorpm/RPM-GPG-KEY/*

%changelog
* Sun May 22 2016 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 1.3-1
- Using rpmbd instead full root environment
- Cleanup code
* Mon Feb 8 2016 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 1.2-1
- Split functions in nekorpm's source code into some files
- Another people can use nekorpm's functions to create new tool. Function's location: /usr/share/nekorpm/functions/
* Sun Nov 15 2015 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 1.1-1
- nekorpm 1.1 release
- add zenity and kdialog to select package
* Tue Aug 18 2015 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 1.0-2
- nekorpm 1.0 release
- Fix URL in SPEC file
- Add --allowerasing DNF option for better dependencies solving.
