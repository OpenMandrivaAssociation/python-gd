%define module	gd
%define name	python-%{module}

Name:		%{name}
Group:		Development/Python
License:	BSD
Summary:	Python GD module
Version:	0.56
Release:	%mkrel 1
Source:		http://newcenturycomputers.net/projects/download.cgi/gdmodule-%{version}.tar.gz
URL:		http://newcenturycomputers.net/projects/gdmodule.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	freetype2-devel
BuildRequires:	libgd-devel >= 2.0.23
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libx11-devel
BuildRequires:	libxpm-devel
BuildRequires:	python-devel
BuildRequires:	zlib-devel
Requires:	gd >= 2.0.23
Requires:	python

%description
This module is a python wrapper for the GD library. Due to the constant
change in the GD library API, there are several older versions of this
module available.

%prep
%setup -q -n gdmodule-%{version}
%ifnarch %{ix86}
perl -pi -e 's|"/usr/local/lib"|"%{_libdir}"|;' Setup.py
%endif

%build

%install
%__python Setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README
