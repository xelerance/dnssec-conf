Summary: DNSSEC and DLV configuration and priming tool
Name: dnssec-conf
Version: 1.22
Release: 1%{?dist}
License: GPLv2+
Url: http://www.xelerance.com/software/dnssec-conf/
Source: http://www.xelerance.com/software/%{name}/%{name}-%{version}.tar.gz
Group: System Environment/Daemons
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Buildrequires: xmlto
Requires: python-dns, curl, pyparsing
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
See also: system-config-dnssec

%prep
%setup -q -n %{name}-%{version}

%build
make 

%install
rm -rf ${RPM_BUILD_ROOT}
make PREFIX=%{_prefix} DESTDIR=${RPM_BUILD_ROOT} ETCDIR=${RPM_BUILD_ROOT}/etc install
install -d 0755 ${RPM_BUILD_ROOT}/%{_sysconfdir}/sysconfig
install -m 0644 packaging/fedora/dnssec.sysconfig ${RPM_BUILD_ROOT}/%{_sysconfdir}/sysconfig/dnssec
%clean
rm -rf ${RPM_BUILD_ROOT}

%files 
%defattr(-,root,root)
%doc LICENSE README INSTALL
%attr(0755,root,root) %dir %{_sysconfdir}/pki/dnssec-keys
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pki/dnssec-keys/*/*
%attr(0755,root,root) %dir %{_sysconfdir}/pki/dnssec-keys/production
%attr(0755,root,root) %dir %{_sysconfdir}/pki/dnssec-keys/production/reverse
%attr(0755,root,root) %dir %{_sysconfdir}/pki/dnssec-keys/testing
%attr(0755,root,root) %dir %{_sysconfdir}/pki/dnssec-keys/harvest
%attr(0755,root,root) %dir %{_sysconfdir}/pki/dnssec-keys/dlv
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/dnssec
%{_bindir}/dnskey-pull
%{_sbindir}/dnssec-configure
%{_mandir}/*/*

%changelog
* Sun Jun 14 2009 Paul Wouters <paul@xelerance.com> - 1.21-1
- upgraded to 1.21

* Tue Mar 17 2009 Paul Wouters <paul@xelerance.com> - 1.20-1
- Upgraded to 1.20, which fixes DLV support for Bind and reverse keys for Bind

* Tue Mar 17 2009 Paul Wouters <paul@xelerance.com> - 1.19-1
- Upgraded to 1.19, which adds --nocheck for the unbound post command.

* Sat Mar 14 2009 Paul Wouters <paul@xelerance.com> - 1.18-1
- Upgraded to 1.18 for new RIPE keys and .th testing key
- Fix for when Bind is installed but Unbound is not
- No longer need the patch - upstream committed it.

* Tue Mar 10 2009 Adam Tkac <atkac redhat com> - 1.17-4
- fixed -b -s command
- added dist tag

* Tue Mar 10 2009 Paul Wouters <paul@xelerance.com> - 1.17-3
- Remove require for unbound. It can also be used with just bind,
  and we don't require it to work.

* Mon Mar 09 2009 Paul Wouters <paul@xelerance.com> - 1.17-2
- Fix build for /etc/sysconfig/dnssec

* Mon Mar 09 2009 Paul Wouters <paul@xelerance.com> - 1.17-1
- Upgraded to 1.17. This adds better initscript support and fixes a bug
  when named/unbound were not installed (rhbug 488685)

* Sun Mar 01 2009 Paul Wouters <paul@xelerance.com> - 1.16-1
- Upgraded to 1.16. This adds the production key for .gov
  See http://dotgov.gov/dnssecinfo.aspx

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb  9 2009 Paul Wouters <paul@xelerance.com> - 1.15-1
- Upgraded to new upstream. Added INSTALL to doc section

* Wed Jan 21 2009 Paul Wouters <paul@xelerance.com> - 1.13-2
- Upstream made source available :=)
- removed macros from changes.

* Wed Jan 21 2009 Paul Wouters <paul@xelerance.com> - 1.13-1
- Clarify license
- Fix mixed use of RPM_BUILD_ROOT and buildroot
- Source tag fully qualified now

* Sat Jan 17 2009 Paul Wouters <paul@xelerance.com> - 1.10-1
- Updated to 1.10. Adds --set and --query and show option to use with system-config-dnssec
- Updated RIPE's reverse keys

* Tue Jan 13 2009 Paul Wouters <paul@xelerance.com> - 1.09-1
- Added testing key for gr.

* Mon Jan  5 2009 Paul Wouters <paul@xelerance.com> 1.08-1
- Upgrade to 'upstream'

* Mon Jan  5 2009 Paul Wouters <paul@xelerance.com> 1.07-1
- Require unbound >= 1.1.1-7

* Mon Jan  5 2009 Paul Wouters <paul@xelerance.com> 1.06-1
- Package renamed to dnssec-conf
- Added punycode test keys
- Fix for dnskey-pull and UTF8
- No longer requires the use of generating .conf files, by using
  a patch for unbound

* Fri Nov  7 2008 Paul Wouters <paul@xelerance.com> 1.0-1
- Initial release

