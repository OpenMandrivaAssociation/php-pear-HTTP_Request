%define		_class		HTTP
%define		_subclass	Request
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.4.4
Release:	%mkrel 7
Summary:	Provides an easy way to perform HTTP requests
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTTP_Request/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-pear-Net_URL >= 1.0.12
Requires:	php-pear-Net_Socket >= 1.0
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Supports GET/POST/HEAD/TRACE/PUT/DELETE, Basic authentication, Proxy,
Proxy Authentication etc.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.4-6mdv2011.0
+ Revision: 667513
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.4-5mdv2011.0
+ Revision: 607111
- rebuild

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.4-4mdv2010.1
+ Revision: 477896
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.4.4-3mdv2010.0
+ Revision: 426647
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.4-2mdv2009.1
+ Revision: 321869
- rebuild

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.4-1mdv2009.1
+ Revision: 305784
- update to new version 1.4.4

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-1mdv2009.0
+ Revision: 272591
- 1.4.3

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.4.1-4mdv2009.0
+ Revision: 224748
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-3mdv2008.1
+ Revision: 178518
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 Thierry Vignaud <tv@mandriva.org> 1.4.1-2mdv2008.0
+ Revision: 64199
- rebuild

* Sun May 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-1mdv2008.0
+ Revision: 28898
- 1.4.1

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-1mdv2008.0
+ Revision: 15545
- 1.4.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2007.0
+ Revision: 81131
- Import php-pear-HTTP_Request

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdk
- new group (Development/PHP)

* Sun Nov 06 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-1mdk
- 1.3.0

* Thu Aug 25 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-8mdk
- rebuilt to fix auto deps

* Thu Aug 18 2005 Andreas Hasenack <andreas@mandriva.com> 1.2.4-7mdk
- included missing file (Listener.php)

* Tue Aug 09 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sat Jul 30 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-5mdk
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-4mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-3mdk
- fix deps

* Mon Jul 18 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-2mdk
- fix spec file to conform with the others

* Thu Jan 20 2005 Pascal Terjan <pterjan@mandrake.org> 1.2.4-1mdk
- First mdk package

