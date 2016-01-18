Name: onerpm
Version: 1.1
Release: 1
URL: https://wonderneko.wordpress.com/
License: GPL
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-root
Requires: bash
Requires: dnf >= 1.0.2
Requires: dnf-plugins-core
Source0: onerpm-%{version}.tar.gz
BuildArch: noarch
Summary: onerpm is a single offline installer for Fedora

%description
onerpm is a single offline installer for Fedora.

%prep
%setup

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
install -m 755 onerpm ${RPM_BUILD_ROOT}%{_bindir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/onerpm

%changelog
* Sun Nov 15 2015 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 1.1-1
- onerpm 1.1 release
- add zenity and kdialog to select package
* Tue Aug 18 2015 La Ode Muh. Fadlun Akbar <fadlun.net@gmail.com> - 1.0-2
- onerpm 1.0 release
- Fix URL in SPEC file
- Add --allowerasing DNF option for better dependencies solving. 
