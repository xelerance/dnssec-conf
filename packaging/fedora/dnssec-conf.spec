Summary: DNSSEC configuration tool and keys for priming recursing nameservers until the root is signed
Name: dnssec-conf
Version: 1.06
Release: 1
License: GPLv2+
Url: http://www.xelerance.com/software/dnssec-conf/
Source: %{name}-%{version}.tar.gz
Group: System Environment/Daemons
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Buildrequires: xmlto
Requires: python-dns, curl, unbound >= 1.1.1-7
Obsoletes: dnssec-keys <= 1.06-1
#Requires: a caching nameserver
#Requires bind 9.4.0 if bind is reconfigured.....

%description
DNSSEC configuration and priming tool. Keys are required until the root
is signed, as well as for local unpublished DNSSEC keys to be preloaded
into the recursive nameserver. These DNSSEC configuration files can be
directly included in the bind or unbound nameserver configuration files.
dnssec-conf includes a commandline configuration client for Bind and
Unbound, known DNSSEC keys, URL's to official publication pages of keys,
and harvested keys, as well a script to harvest DNSKEY's from DNS.

%prep
%setup -q -n %{name}-%{version}

%build
make 

%install
rm -rf %{buildroot}
make DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf ${RPM_BUILD_ROOT}

%files 
%defattr(-,root,root)
%doc LICENSE README
%attr(0755,root,root) %dir %{_sysconfdir}/pki/dnssec-keys
%attr(0644,root,root) %config %{_sysconfdir}/pki/dnssec-keys/*/*
%attr(0755,root,root) %dir %{_sysconfdir}/pki/dnssec-keys/production
%attr(0755,root,root) %dir %{_sysconfdir}/pki/dnssec-keys/production/reverse
%attr(0755,root,root) %dir %{_sysconfdir}/pki/dnssec-keys/testing
%attr(0755,root,root) %dir %{_sysconfdir}/pki/dnssec-keys/harvest
%attr(0755,root,root) %dir %{_sysconfdir}/pki/dnssec-keys/dlv
%{_bindir}/dnskey-pull
%{_sbindir}/dnssec-configure
%{_mandir}/*/*

%changelog
* Mon Jan  5 2009 Paul Wouters <paul@xelerance.com> 1.06-1
- Package renamed to dnssec-conf
- Added punycode test keys
- Fix for dnskey-pull and UTF8
- No longer requires the use of generating .conf files, by using
  a patch for unbound

* Fri Nov  7 2008 Paul Wouters <paul@xelerance.com> 1.0-1
- Initial release

