#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : requests
Version  : 2.21.0
Release  : 69
URL      : https://files.pythonhosted.org/packages/52/2c/514e4ac25da2b08ca5a464c50463682126385c4272c18193876e91f4bc38/requests-2.21.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/52/2c/514e4ac25da2b08ca5a464c50463682126385c4272c18193876e91f4bc38/requests-2.21.0.tar.gz
Summary  : Python HTTP for Humans.
Group    : Development/Tools
License  : Apache-2.0
Requires: requests-license = %{version}-%{release}
Requires: requests-python = %{version}-%{release}
Requires: requests-python3 = %{version}-%{release}
Requires: certifi
Requires: chardet
Requires: idna
Requires: urllib3
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : setuptools
BuildRequires : setuptools-legacypython

%description
==========================

%package legacypython
Summary: legacypython components for the requests package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the requests package.


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

%description python3
python3 components for the requests package.


%prep
%setup -q -n requests-2.21.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546111786
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python test_requests.py || :
%install
export SOURCE_DATE_EPOCH=1546111786
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/requests
cp LICENSE %{buildroot}/usr/share/package-licenses/requests/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/requests/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
