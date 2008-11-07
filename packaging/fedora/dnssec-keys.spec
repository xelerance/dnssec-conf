Summary: DNSSEC keys for priming recursing nameservers until the root is signed
Name: dnssec-keys
Version: 1.01
Release: 1
License: Copyright 2005-2008 Xelerance corporation, All rights reserved
Url: http://www.xelerance.com/dnssec/
Source: %{name}-%{version}.tar.gz
Group: System Environment/Daemons
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#Requires: a caching nameserver

%description
DNSSEC keys for priming recursing nameservers until the root is signed. These
files can be directly included in the bind or unbound nameserver configuration
files.
This package includes known keys, URL's to official publication pages
of keys, and harvested keys, as well a script to harvest DNSKEY's from DNS.

%prep
rm -rf ${RPM_BUILD_ROOT}
%setup -q -n %{name}-%{version}

%build
cat production/*.conf > production.conf
cat testing/*.conf > testing.conf

%install
install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/pki/%{name}/

install -p -D -m644 production.conf ${RPM_BUILD_ROOT}%{_sysconfdir/pki/production.conf
install -p -D -m644 testing.conf ${RPM_BUILD_ROOT}%{_sysconfdir/pki/testing.conf

%clean
rm -rf ${RPM_BUILD_ROOT}

%files 
%defattr(-,root,root)
%doc LICENSE 
%attr(0644,root,root) %dir %{_sysconfdir}/pki/%{name}

%changelog
* Fri Nov  7 2008 Paul Wouters <paul@xelerance.com> 1.01-1
- Updated spec file for the doc buglet and the new directory layouts
