%global packname rattle
%global packrel 1
%global debug_package %{nil}

Name:             R-%{packname}
Version:          4.0.5
Release:          1%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{version}.tar.gz
License:          GPLv2+
URL:              http://cran.r-project.org/src/contrib
Group:            Applications/Engineering
Summary:          Adds foo functionality for R
BuildRequires:    R-devel, tex(latex), texlive-lastpage, R-stringi,  R-magrittr, R-RGtk2
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
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/CITATION
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/csv
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/data
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/etc
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/odt
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/po
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/po/de
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/po/es
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/po/fr
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/po/id
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/po/ja
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/po/no
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/po/zh_CN



%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css

%check
#%{_bindir}/R CMD check %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/arff/audit.arff
%{_libdir}/R/library/%{packname}/arff/weather.arff
%{_libdir}/R/library/%{packname}/csv/audit.csv
%{_libdir}/R/library/%{packname}/csv/dvdtrans.csv
%{_libdir}/R/library/%{packname}/csv/weather.csv
%{_libdir}/R/library/%{packname}/data/Rdata.rdb
%{_libdir}/R/library/%{packname}/data/Rdata.rds
%{_libdir}/R/library/%{packname}/data/Rdata.rdx
%{_libdir}/R/library/%{packname}/data/datalist
%{_libdir}/R/library/%{packname}/etc/ConnectRlogo.png
%{_libdir}/R/library/%{packname}/etc/Rlogo.png
%{_libdir}/R/library/%{packname}/etc/gpl-license
%{_libdir}/R/library/%{packname}/etc/rattle.glade
%{_libdir}/R/library/%{packname}/etc/rattle.ui
%{_libdir}/R/library/%{packname}/etc/rattle_macosx.ui
%{_libdir}/R/library/%{packname}/etc/textviews.xml
%{_libdir}/R/library/%{packname}/etc/tooltips.xml
%{_libdir}/R/library/%{packname}/odt/data_summary.odt
%{_libdir}/R/library/%{packname}/po/de/LC_MESSAGES/R-rattle.mo
%{_libdir}/R/library/%{packname}/po/es/LC_MESSAGES/R-rattle.mo
%{_libdir}/R/library/%{packname}/po/fr/LC_MESSAGES/R-rattle.mo
%{_libdir}/R/library/%{packname}/po/id/LC_MESSAGES/R-rattle.mo
%{_libdir}/R/library/%{packname}/po/ja/LC_MESSAGES/R-rattle.mo
%{_libdir}/R/library/%{packname}/po/no/LC_MESSAGES/R-rattle.mo
%{_libdir}/R/library/%{packname}/po/zh_CN/LC_MESSAGES/R-rattle.mo

%changelog
* Sat Jan 23 2016 konstantinjch <konstantinjch@yandex.ru> 1.0-1
- Initial package creation
