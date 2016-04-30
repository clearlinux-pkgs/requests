#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : requests
Version  : 2.8.1
Release  : 22
URL      : https://pypi.python.org/packages/source/r/requests/requests-2.8.1.tar.gz
Source0  : https://pypi.python.org/packages/source/r/requests/requests-2.8.1.tar.gz
Summary  : Python HTTP for Humans.
Group    : Development/Tools
License  : Apache-2.0
Requires: requests-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Requests: HTTP for Humans
=========================
.. image:: https://img.shields.io/pypi/v/requests.svg
:target: https://pypi.python.org/pypi/requests

%package python
Summary: python components for the requests package.
Group: Default

%description python
python components for the requests package.


%prep
%setup -q -n requests-2.8.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python test_requests.py || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
