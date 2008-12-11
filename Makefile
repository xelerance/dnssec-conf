# A bit overkill, but rpm does not like redirecting output?
#

DESTDIR?=
ETCDIR?=/etc
BINDIR?=/usr/bin
SBINDIR?=/usr/sbin
MANDIR?=/usr//share/man
KEYSDIR?=/etc/pki/dnssec-keys

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
	mkdir -m0755 -p $(DESTDIR)/$(BINDIR) $(DESTDIR)/$(SBINDIR) $(DESTDIR)/$(MANDIR)/man1 $(DESTDIR)/$(MANDIR)/man8 $(DESTDIR)/$(KEYSDIR)
	install -m 0755 dnskey-pull $(DESTDIR)/$(BINDIR)
	install -m 0755 dnssec-configure $(DESTDIR)/$(SBINDIR)
	install -m 0644 dnskey-pull.1 $(DESTDIR)/$(MANDIR)/man1/
	install -m 0644 dnssec-configure.8 $(DESTDIR)/$(MANDIR)/man8/
	cp -a production testing harvest dlv $(DESTDIR)/$(KEYSDIR)/
	cp -a *.conf $(DESTDIR)/$(KEYSDIR)/
	@echo
	@echo "Run dnssec-configure to enable one or more Trusted Keys repositories and DNSSEC and/or DLV options."
	@echo


