# A bit overkill, but rpm does not like redirecting output?
#

PREFIX?=/usr/local
DESTDIR?=
ETCDIR?=$(DESTDIR)/$(PREFIX)/etc
KEYSDIR?=$(ETCDIR)/pki/dnssec-keys
BINDIR?=$(DESTDIR)/$(PREFIX)/bin
SBINDIR?=$(DESTDIR)/$(PREFIX)/sbin
MANDIR?=$(DESTDIR)/$(PREFIX)/share/man

all:	manpages

manpages: dnskey-pull.1 dnssec-configure.8

dnskey-pull.1:
	xmlto man dnskey-pull.1.xml

dnssec-configure.8:
	xmlto man dnssec-configure.8.xml

clean:
	rm -f *.1 *.8

install:
	mkdir -m0755 -p $(BINDIR) $(SBINDIR) $(MANDIR)/man1 $(MANDIR)/man8 $(KEYSDIR)
	install -m 0755 dnskey-pull $(BINDIR)
	install -m 0755 dnssec-configure $(SBINDIR)
	install -m 0644 dnskey-pull.1 $(MANDIR)/man1/
	install -m 0644 dnssec-configure.8 $(MANDIR)/man8/
	cp -r production harvest dlv $(KEYSDIR)/
	@echo
	@echo "Run dnssec-configure to enable one or more Trusted Keys repositories and DNSSEC and/or DLV options."
	@echo


