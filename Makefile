# A bit overkill, but rpm does not like redirecting output?
#

DESTDIR?=/usr/local

MANDIR?=/usr/local/man

all:	production.conf testing.conf harvest.conf manpages

manpages: dnskey-pull.1 dnssec-configure.1

dnskey-pull.1:
	xmlto man dnskey-pull.1.xml

dnssec-configure.1:
	xmlto man dnssec-configure.1.xml

production.conf:
	cat production/*.conf > production.conf

testing.conf:
	cat testing/*.conf > testing.conf

harvest.conf:
	cat harvest/*.conf > harvest.conf

cleanall:
	rm -f production.conf testing.conf harvest.conf harvest/*.conf *.1

clean:
	rm -f production.conf testing.conf harvest.conf *.1

install:
	mkdir -p $(DESTDIR)/bin/ $(MANDIR)/man1/
	install -m 0755 dnskey-pull $(DESTDIR)/bin/
	install -m 0644 dnskey-pull.1 $(MANDIR)/man1/
	@echo
	@echo "To include the production.conf keys for or unbound, copy the file into"
	@echo "the nameserver's configuration directory, and include the file in the"
	@echo "configuration. Note that sometimes files are copied into a chroot."
	@echo
	@echo "For named, add the following line to named.conf:"
	@echo
	@echo "		include \"/etc/bind/production.conf\";"
	@echo
	@echo "For unbound, add the following line to unbound.conf's 'server' section:"
	@echo
	@echo "		trusted-keys-file: \"/var/lib/unbound/production.conf\"";


