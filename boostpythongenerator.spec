Name: boostpythongenerator
Version: 0.2
Release: %mkrel 1
License: LGPLv2+
Summary:  Binding Generator utility that parses the headers for a given C/C++
Group: Development/KDE and Qt
URL: http://www.pyside.org
Source0:  %name-%version.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: cmake
BuildRequires: qt4-devel
BuildRequires: boost-devel
BuildRequires: apiextractor-devel >= 0.2
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

%prep
%setup -q

%build
%cmake
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %buildroot

