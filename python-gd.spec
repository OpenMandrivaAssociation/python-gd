%define module	gd
%define name	python-%{module}

Name:		%{name}
Group:		Development/Python
License:	BSD
Summary:	Python GD module
Version:	0.56
Release:	%mkrel 3
Source:		http://newcenturycomputers.net/projects/download.cgi/gdmodule-%{version}.tar.gz
URL:		http://newcenturycomputers.net/projects/gdmodule.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	freetype2-devel
BuildRequires:	gd-devel = 2.0.35-22 >= 2.0.23
BuildRequires:	jpeg-devel = 1:1.2.1-5:2013.0
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)
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
PYTHONDONTWRITEBYTECODE= \
%__python Setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README


%changelog
* Sun Nov 06 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.56-3mdv2012.0
+ Revision: 722026
- Rebuild with newer libpng.

* Thu Nov 04 2010 Paulo Andrade <pcpa@mandriva.com.br> 0.56-2mdv2011.0
+ Revision: 593487
+ rebuild (emptylog)

* Mon Aug 17 2009 Oden Eriksson <oeriksson@mandriva.com> 0.56-2mdv2010.0
+ Revision: 417295
- rebuilt against libjpeg v7

* Wed Mar 11 2009 Paulo Andrade <pcpa@mandriva.com.br> 0.56-1mdv2009.1
+ Revision: 353555
- Initial import of python-gd 0.56.
  A Python wrapper for the GD library.
- python-gd

