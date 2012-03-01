%define		modname	tidy
%define		php_sysconfdir	/etc/php
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)
Summary:	%{modname} - Tidy HTML Repairing and Parsing
Summary(pl.UTF-8):	%{modname} - Czyszczenie, naprawa oraz parsowanie HTML
Name:		php-pecl-%{modname}
Version:	1.2
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	8c1c92d9386c56d483b1115d207c0293
URL:		http://pecl.php.net/package/tidy/
BuildRequires:	php-devel >= 4:5.0.4
BuildRequires:	rpmbuild(macros) >= 1.519
BuildRequires:	tidy-devel
%{?requires_php_extension}
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tidy is a binding for the Tidy HTML clean and repair utility which
allows you to not only clean and otherwise manipluate HTML documents,
but also traverse the document tree using the Zend Engine 2 OO
semantics.

%description -l pl.UTF-8
Tidy jest dowiązaniem do narzędzia "Tidy HTML clean and repair", które
pozwala nie tylko na czyszczenie oraz manipulację dokumentami HTML,
ale także na przemierzanie przez strukturę dokumentu za pomocą
zorientowanej obiektowo semantyki silnika Zend Engine 2.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d
%{__make} install \
	EXTENSION_DIR=%{php_extensiondir} \
	INSTALL_ROOT=$RPM_BUILD_ROOT
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS TODO README
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{extensionsdir}/%{modname}.so
