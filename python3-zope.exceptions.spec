#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests

%define	module	zope.exceptions
Summary:	Zope Exceptions
Summary(pl.UTF-8):	Zope Exceptions - wyjątki Zope
Name:		python3-%{module}
Version:	5.2
Release:	1
License:	ZPL v2.1
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/zope-exceptions/
Source0:	https://files.pythonhosted.org/packages/source/z/zope.exceptions/zope.exceptions-%{version}.tar.gz
# Source0-md5:	26167cb6f437f39a8299fcf2c6af0021
URL:		https://www.zope.org/
BuildRequires:	python3 >= 1:3.8
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-zope.interface
BuildRequires:	python3-zope.testrunner
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
BuildRequires:	python3-repoze.sphinx.autointerface
%endif
Requires:	python3-modules >= 1:3.8
Requires:	python3-zope-base
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
%py3_build

%if %{with tests}
%{__python3} -m zope.testrunner --test-path=src
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install
#	--install-purelib=%{py3_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%{py3_sitescriptdir}/zope/exceptions
%{py3_sitescriptdir}/zope.exceptions-%{version}-py*.egg-info
%{py3_sitescriptdir}/zope.exceptions-%{version}-py*-nspkg.pth

%if %{with doc}
%defattr(644,root,root,755)
%files apidocs
%doc docs/_build/html/{_static,*.html,*.js}
%endif
