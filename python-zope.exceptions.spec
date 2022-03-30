#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define	module	zope.exceptions
Summary:	Zope Exceptions
Summary(pl.UTF-8):	Zope Exceptions - wyjątki Zope
Name:		python-%{module}
Version:	4.5
Release:	3
License:	ZPL v2.1
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/zope-exceptions/
Source0:	https://files.pythonhosted.org/packages/source/z/zope.exceptions/zope.exceptions-%{version}.tar.gz
# Source0-md5:	e03b67ab2ac46591fde926b0044a6636
URL:		https://www.zope.org/
%if %{with python2}
BuildRequires:	python >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-zope.interface
BuildRequires:	python-zope.testrunner
%endif
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-zope.interface
BuildRequires:	python3-zope.testrunner
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
BuildRequires:	python3-repoze.sphinx.autointerface
%endif
Requires:	python-modules >= 1:2.7
Requires:	python-zope-base
Obsoletes:	Zope-Exceptions < 4.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains exception exceptions and implementations which
are so general purpose that they don't belong in Zope
application-specific packages.

%description -l pl.UTF-8
Ten pakiet zawiera wyjątki oraz implementacje wyjątków, mających na
tyle ogólne zastosowanie, że nie należą do żadnego z pakietów Zope
specyficznych dla aplikacji.

%package -n python3-%{module}
Summary:	Zope Exceptions
Summary(pl.UTF-8):	Zope Exceptions - wyjątki Zope
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5
Requires:	python3-zope-base

%description -n python3-%{module}
This package contains exception exceptions and implementations which
are so general purpose that they don't belong in Zope
application-specific packages.

%description -n python3-%{module} -l pl.UTF-8
Ten pakiet zawiera wyjątki oraz implementacje wyjątków, mających na
tyle ogólne zastosowanie, że nie należą do żadnego z pakietów Zope
specyficznych dla aplikacji.

%package apidocs
Summary:	API documentation for Python zope.exceptions module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona zope.exceptions
Group:		Documentation

%description apidocs
API documentation for Python zope.exceptions module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona zope.exceptions.

%prep
%setup -q -n zope.exceptions-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m zope.testrunner --test-path=src
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m zope.testrunner --test-path=src
%endif
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install \
	--install-purelib=%{py_sitescriptdir}
%py_postclean
%endif

%if %{with python3}
%py3_install \
	--install-purelib=%{py3_sitescriptdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%{py_sitescriptdir}/zope/exceptions
%{py_sitescriptdir}/zope.exceptions-%{version}-py*.egg-info
%{py_sitescriptdir}/zope.exceptions-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%{py3_sitescriptdir}/zope/exceptions
%{py3_sitescriptdir}/zope.exceptions-%{version}-py*.egg-info
%{py3_sitescriptdir}/zope.exceptions-%{version}-py*-nspkg.pth
%endif

%if %{with doc}
%defattr(644,root,root,755)
%files apidocs
%doc docs/_build/html/{_static,*.html,*.js}
%endif
