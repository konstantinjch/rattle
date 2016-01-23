%global packname  	stringi

Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Source0:        ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{version}-1.tar.gz
License:          GPLv2+
URL:              http://cran.r-project.org/src/contrib
Group:            Applications/Engineering
Summary:          Adds foo functionality for R
BuildRequires:    R-devel, tex(latex)
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:         R-core

%description
R Interface to foo, enables bar!

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css

%check
%{_bindir}/R CMD check %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/AUTHORS
%{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/LICENSE
%{_libdir}/R/library/%{packname}/include/stringi.cpp
%{_libdir}/R/library/%{packname}/include/stringi.h
%{_libdir}/R/library/%{packname}/libs/stringi.so
%{_libdir}/R/library/%{packname}/help

%changelog
* Sat Jan 23 2016 konstantinjch <konstantinjch@yandex.ru> 1.0-1
- Initial package creation

