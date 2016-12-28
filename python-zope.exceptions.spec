#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define	module	zope.exceptions
Summary:	Zope Exceptions
Name:		python-%{module}
Version:	4.0.8
Release:	2
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/8f/b7/eba9eca6841fa47d9a30f71a602be7615bff4f8e11f85c2840b88a77c68a/zope.exceptions-4.0.8.tar.gz
# Source0-md5:	c6f9b3905a48ba0487f82d95fba71c0c
URL:		http://www.zope.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-setuptools
%endif
%pyrequires_eq	python-modules
Obsoletes:	Zope-Exceptions
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains exception exceptions and implementations which are so
general purpose that they don’t belong in Zope application-specific packages.

%package -n python3-%{module}
Summary:	Zope Exceptions
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
This package contains exception exceptions and implementations which are so
general purpose that they don’t belong in Zope application-specific packages.

%prep
%setup -q -n zope.exceptions-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install \
	--install-purelib=%{py_sitedir}
%py_postclean
%endif

%if %{with python3}
%py3_install \
	--install-purelib=%{py3_sitedir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitedir}/zope/exceptions
%{py_sitedir}/zope.exceptions-*.egg-info
%{py_sitedir}/zope.exceptions-*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitedir}/zope/exceptions
%{py3_sitedir}/zope.exceptions-*.egg-info
%{py3_sitedir}/zope.exceptions-*-nspkg.pth
%endif
