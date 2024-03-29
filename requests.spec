#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : requests
Version  : 2.27.0
Release  : 106
URL      : https://files.pythonhosted.org/packages/c0/e3/826e27b942352a74b656e8f58b4dc7ed9495ce2d4eeb498181167c615303/requests-2.27.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c0/e3/826e27b942352a74b656e8f58b4dc7ed9495ce2d4eeb498181167c615303/requests-2.27.0.tar.gz
Summary  : Python HTTP for Humans.
Group    : Development/Tools
License  : Apache-2.0
Requires: requests-license = %{version}-%{release}
Requires: requests-python = %{version}-%{release}
Requires: requests-python3 = %{version}-%{release}
Requires: charset-normalizer
Requires: urllib3
BuildRequires : buildreq-distutils3
BuildRequires : charset-normalizer
BuildRequires : pypi(certifi)
BuildRequires : pypi(urllib3)

%description
**Requests** is a simple, yet elegant, HTTP library.
        
        ```python
        >>> import requests

%package license
Summary: license components for the requests package.
Group: Default

%description license
license components for the requests package.


%package python
Summary: python components for the requests package.
Group: Default
Requires: requests-python3 = %{version}-%{release}

%description python
python components for the requests package.


%package python3
Summary: python3 components for the requests package.
Group: Default
Requires: python3-core
Provides: pypi(requests)
Requires: pypi(certifi)
Requires: pypi(charset_normalizer)
Requires: pypi(idna)
Requires: pypi(urllib3)

%description python3
python3 components for the requests package.


%prep
%setup -q -n requests-2.27.0
cd %{_builddir}/requests-2.27.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641237417
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python test_requests.py || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/requests
cp %{_builddir}/requests-2.27.0/LICENSE %{buildroot}/usr/share/package-licenses/requests/57aed0b0f74e63f6b85cce11bce29ba1710b422b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/requests/57aed0b0f74e63f6b85cce11bce29ba1710b422b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
