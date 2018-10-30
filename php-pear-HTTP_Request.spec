%define _class		HTTP
%define _subclass	Request
%define modname	%{_class}_%{_subclass}

Summary:	Provides an easy way to perform HTTP requests
Name:		php-pear-%{modname}
Version:	1.4.4
Release:	17
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/HTTP_Request/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear
Requires:	php-pear-Net_URL >= 1.0.12
Requires:	php-pear-Net_Socket >= 1.0

%description
Supports GET/POST/HEAD/TRACE/PUT/DELETE, Basic authentication, Proxy,
Proxy Authentication etc.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

