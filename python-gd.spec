%define module	gd

Name:		python-%{module}
Version:	0.56
Release:	6
Group:		Development/Python
License:	BSD
Summary:	Python GD module
Source:		http://newcenturycomputers.net/projects/download.cgi/gdmodule-%{version}.tar.gz
URL:		http://newcenturycomputers.net/projects/gdmodule.html

BuildRequires:	pkgconfig(freetype2)
BuildRequires:	gd-devel >= 2.0.35-22
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	python-devel
BuildRequires:	zlib-devel
Requires:	gd >= 2.0.35
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
PYTHONDONTWRITEBYTECODE= \
%__python Setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc README
