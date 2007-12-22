%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	US
%define		_status		beta
%define		_pearname	Validate_US

Summary:	%{_pearname} - Validation class for US
Summary(pl.UTF-8):	%{_pearname} - Klasa sprawdzająca poprawność dla Stanów Zjednoczonych
Name:		php-pear-%{_pearname}
Version:	0.5.3
Release:	1
Epoch:		0
License:	new BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2fcebb63f2104221601d44b6e7496bfe
URL:		http://pear.php.net/package/Validate_US/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for US such as:
- SSN
- Postal Code
- Regions (States)
- Phone Numbers

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Stanów Zjednocznych danych
takich jak:
- numer ubezpieczenia społecznego (SSN)
- kod pocztowy
- region (stan)
- numer telefonu

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/US.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Validate_US
