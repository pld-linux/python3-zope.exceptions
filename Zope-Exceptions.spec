Summary:	Zope Exceptions
Name:		Zope-Exceptions
Version:	4.0.8
Release:	1
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/8f/b7/eba9eca6841fa47d9a30f71a602be7615bff4f8e11f85c2840b88a77c68a/zope.exceptions-4.0.8.tar.gz
# Source0-md5:	c6f9b3905a48ba0487f82d95fba71c0c
URL:		http://www.zope.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains exception exceptions and implementations which are so
general purpose that they don’t belong in Zope application-specific packages.

%prep
%setup -q -n zope.exceptions-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--install-purelib=%{py_sitedir} \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/zope/exceptions
%{py_sitedir}/zope.exceptions-*.egg-info
%{py_sitedir}/zope.exceptions-*-nspkg.pth
