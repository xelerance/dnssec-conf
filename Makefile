# A bit overkill, but rpm does not like redirecting output?
#

DESTDIR?=/usr/local
ETCDIR?=/etc

MANDIR?=/usr/local/share/man

all:	production.conf testing.conf harvest.conf manpages

manpages: dnskey-pull.1 dnssec-configure.8

dnskey-pull.1:
	xmlto man dnskey-pull.1.xml

dnssec-configure.8:
	xmlto man dnssec-configure.8.xml

production.conf:
	cat production/*.conf production/reverse/*.conf > production.conf

testing.conf:
	cat testing/*.conf > testing.conf

harvest.conf:
	cat harvest/*.conf > harvest.conf


clean:
	rm -f production.conf testing.conf harvest.conf *.1 *.8

install:
	mkdir -p $(DESTDIR)/bin $(DESTDIR)/sbin $(MANDIR)/man1 $(MANDIR)/man8
	install -m 0755 dnskey-pull $(DESTDIR)/bin/
	install -m 0755 dnssec-configure $(DESTDIR)/sbin/
	install -m 0644 dnskey-pull.1 $(MANDIR)/man1/
	install -m 0644 dnssec-configure.8 $(MANDIR)/man8/
	@echo
	@echo "Run dnssec-configure to enable one or more Trusted Keys repositories and DNSSEC and/or DLV options."
	@echo


