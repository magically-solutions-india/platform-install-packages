%define python27_sitelib %(python -c "from distutils.sysconfig import get_python_lib; import sys; sys.stdout.write(get_python_lib())")
%{!?py2ver: %global py2ver %(python -c "import sys ; print sys.version[:3]")}
%filter_from_requires s|^python(abi)|python27-python(abi)|
%filter_setup

%global modname schedule

Name:           python27-python-%{modname}
Summary:        Job scheduling for humans
Version:        0.5.0
Release:        3
License:        MIT
Group:          System Environment/Libraries
URL:            https://github.com/dbader/schedule
Source0:        %{modname}-%{version}.tar.gz


BuildArch:      noarch
BuildRequires:  python27-scldevel
BuildRequires:  python27-python-setuptools
#BuildRequires:  setuptools
Requires: python27-python


%description
An in-process scheduler for periodic jobs that uses the builder pattern for configuration. 
Schedule lets you run Python functions (or any other callable) periodically at pre-determined 
intervals using a simple, human-friendly syntax.

%prep
%setup -q -n %{modname}-%{version}



%build
python setup.py build 


%install
%{__mkdir} -p %{buildroot}%{python27_sitelib}/%{modname}
python setup.py install --skip-build --root %{buildroot}
cp -p %{modname}/__init__.py %{buildroot}%{python27_sitelib}/%{modname}/
ls -al %{buildroot}%{python27_sitelib}/%{modname}/


%check
#python setup.py test


%files
%{python27_sitelib}/%{modname}/*
%{python27_sitelib}/%{modname}-%{version}-py2.7.egg-info


%changelog
* Wed Dec 13 2017 Jess Portnoy <jess.portnoy@kaltura.com> - 0.5.0-1
- First release

