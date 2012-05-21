%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global modname tw2.jquery

Name:           python-tw2-jquery
Version:        2.0.2
Release:        2%{?dist}
Summary:        jQuery for ToscaWidgets2

Group:          Development/Languages
License:        MIT
URL:            http://toscawidgets.org
Source0:        http://pypi.python.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

# For building, generally
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%if %{?rhel}%{!?rhel:0} >= 6
BuildRequires:  python-webob1.0 >= 0.9.7
%else
BuildRequires:  python-webob >= 0.9.7
%endif
BuildRequires:  python-tw2-core
BuildRequires:  python-tw2-forms
BuildRequires:  python-paste-deploy

# Specifically for the test suite
BuildRequires:  python-nose
BuildRequires:  python-coverage
BuildRequires:  python-BeautifulSoup
BuildRequires:  python-formencode
BuildRequires:  python-webtest
BuildRequires:  python-strainer

# Templating languages for the test suite
BuildRequires:  python-mako
BuildRequires:  python-genshi


# Runtime requirements
Requires:       python-tw2-core
Requires:       python-tw2-forms

%description
toscawidgets2 (tw2) aims to be a practical and useful widgets framework
that helps people build interactive websites with compelling features, faster
and easier. Widgets are re-usable web components that can include a template,
server-side code and JavaScripts/CSS resources. The library aims to be:
flexible, reliable, documented, performant, and as simple as possible.

jQuery is a fast and concise JavaScript Library that simplifies HTML
document traversing, event handling, animating, and Ajax interactions
for rapid web development. jQuery is designed to change the way that
you write JavaScript.

This module, tw2.jquery, provides toscawidgets2 (tw2) access to the
jQuery library, a namespace package for jQuery plugins, and convenience
classes for creating these plugins.

%prep
%setup -q -n %{modname}-%{version}

%if %{?rhel}%{!?rhel:0} >= 6

# Make sure that epel/rhel picks up the correct version of webob
awk 'NR==1{print "import __main__; __main__.__requires__ = __requires__ = [\"WebOb>=1.0\"]; import pkg_resources"}1' setup.py > setup.py.tmp
mv setup.py.tmp setup.py

# Remove all the fancy nosetests configuration for older python
rm setup.cfg

%endif


%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build \
    --install-data=%{_datadir} --root %{buildroot}

%check
PYTHONPATH=$(pwd) python setup.py test

%files
%doc README.rst LICENSE.txt
%{python_sitelib}/*

%changelog
* Wed May 02 2012 Ralph Bean <rbean@redhat.com> - 2.0.2-2
- Removed clean section
- Removed defattr in files section
- Removed unnecessary references to buildroot

* Wed Apr 11 2012 Ralph Bean <rbean@redhat.com> - 2.0.2-1
- Packaging latest release.
- Fixing a collision of the tests.
- Added awk line to make sure pkg_resources picks up the right WebOb on el6


* Wed Apr 11 2012 Ralph Bean <rbean@redhat.com> - 2.0.1-2
- Fixed typo in Summary.  Forms -> jQuery

* Wed Apr 11 2012 Ralph Bean <rbean@redhat.com> - 2.0.1-1
- Initial packaging for Fedora
