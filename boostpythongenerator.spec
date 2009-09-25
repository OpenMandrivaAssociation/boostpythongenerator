Name: boostpythongenerator
Version: 0.3
Release: %mkrel 1
License: GPLv2
Summary:  Binding Generator utility that parses the headers for a given C/C++
Group: Development/KDE and Qt
URL: http://www.pyside.org
Source0:  %name-%version.tar.bz2
Patch0: boostpythongenerator-0.3-cmake-install-module.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: cmake
BuildRequires: qt4-devel
BuildRequires: boost-devel
BuildRequires: apiextractor-devel >= 0.3
BuildRequires: openssl-devel

%description
The Binding Generator is a utility that parses the headers for a given C/C++
library and modifies this data with the information and guides from XML files
(called typesystem files) containing complementar semantic information,
modifications, renamings, etc, in order to generate binding source code (or
documentation, or anything you want) for the target language for which it was
written.

%files 
%defattr(-,root,root,-)
%_bindir/*

#------------------------------------------------------------------------------

%define libgen_major 0
%define libgen %mklibname genrunner %{libgen_major}

%package -n %{libgen}
Summary: boostpythongenerator core lib
Group: System/Libraries

%description -n %{libgen}
Boostpythongenerator core lib.

%files -n %{libgen}
%defattr(-,root,root)
%{_libdir}/libgenrunner.so.%{libgen_major}*
%{_libdir}/libqtdoc_generator.so
%{_libdir}/libboostpython_generator.so

#------------------------------------------------------------------------------

%package devel
Summary: Devel stuff for boostpythongenerator
Group: Development/KDE and Qt
Requires: %{libgen} = %{version}
Requires: apiextractor-devel >= 0.3
Requires: %name = %{version}

%description devel
Devel stuff for boostpythongenerator.

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libgenrunner.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/Modules/*

#------------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0 -b .orig

%build
%cmake
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %buildroot

