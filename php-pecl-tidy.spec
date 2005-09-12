%define		_modname	tidy
%define		_status		stable

Summary:	%{_modname} - Tidy HTML Repairing and Parsing
Summary(pl):	%{_modname} - Czyszczenie, naprawa oraz parsowanie HTML
Name:		php-pecl-%{_modname}
Version:	1.1
Release:	0.1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	ecb2d3c62e1d720265a65dfb7e00e081
URL:		http://pecl.php.net/package/tidy/
BuildRequires:	libtool
BuildRequires:	php-devel
BuildRequires:	tidy-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
Tidy is a binding for the Tidy HTML clean and repair utility which
allows you to not only clean and otherwise manipluate HTML documents,
but also traverse the document tree using the Zend Engine 2 OO
semantics.

In PECL status of this package is: %{_status}.

%description -l pl
Tidy jest dowi±zaniem do narzêdzia "Tidy HTML clean and repair", które
pozwala nie tylko na czyszczenie oraz manipulacjê dokumentami HTML,
ale tak¿e na przemierzanie przez strukturê dokumentu za pomoc±
zorientowanej obiektowo semantyki silnika Zend Engine 2.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd %{_modname}-%{version}
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,TODO,README}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
