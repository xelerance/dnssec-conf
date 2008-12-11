Summary: DNSSEC keys for priming recursing nameservers until the root is signed
Name: dnssec-keys
Version: 1.0
Release: 1
License: GPLv2+
Url: http://www.xelerance.com/software/dnssec-keys/
Source: %{name}-%{version}.tar.gz
Group: System Environment/Daemons
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires: python-dns
#Requires: a caching nameserver
#Requires bind 9.4.0 if bind is reconfigured.....

%description
DNSSEC keys for priming recursing nameservers until the root is signed. These
files can be directly included in the bind or unbound nameserver configuration
files.
This package includes known keys, URL's to official publication pages
of keys, and harvested keys, as well a script to harvest DNSKEY's from DNS.

%prep
%setup -q -n %{name}-%{version}

%build
make 

%install
make install

%clean
rm -rf ${RPM_BUILD_ROOT}

%files 
%defattr(-,root,root)
%doc LICENSE README
%attr(0755,root,root) %dir %{_sysconfdir}/pki/%{name}
%attr(0755,root,root) %dir %{_sysconfdir}/pki/%{name}/production
%attr(0644,root,root) %{_sysconfdir}/pki/%{name}/production/*.conf
%attr(0755,root,root) %dir %{_sysconfdir}/pki/%{name}/testing
%attr(0644,root,root) %{_sysconfdir}/pki/%{name}/testing/*.conf
%attr(0755,root,root) %dir %{_sysconfdir}/pki/%{name}/harvest
%attr(0644,root,root) %{_sysconfdir}/pki/%{name}/harvest/*.conf
%attr(0755,root,root) %dir %{_sysconfdir}/pki/%{name}/dlv
%attr(0644,root,root) %{_sysconfdir}/pki/%{name}/dlv/*
%attr(0644,root,root) %config %{_sysconfdir}/pki/%{name}/*.conf
%{_bindir}/dnskey-pull
%{_sbindir}/dnssec-configure
%{_mandir}/*/*

%changelog
* Fri Nov  7 2008 Paul Wouters <paul@xelerance.com> 1.01-1 -
- Initial release

