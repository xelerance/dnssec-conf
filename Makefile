# A bit overkill, but rpm does not like redirecting output?
#

PREFIX?=/usr/local
DESTDIR?=
ETCDIR?=$(DESTDIR)/$(PREFIX)/etc
KEYSDIR?=$(ETCDIR)/pki/dnssec-keys
BINDIR?=$(DESTDIR)/$(PREFIX)/bin
SBINDIR?=$(DESTDIR)/$(PREFIX)/sbin
MANDIR?=$(DESTDIR)/$(PREFIX)/share/man
KEYSDIR?=$(ETCDIR)/pki/dnssec-keys

all:	manpages

manpages: dnskey-pull.1 dnssec-configure.8

dnskey-pull.1:
	xmlto man dnskey-pull.1.xml

dnssec-configure.8:
	xmlto man dnssec-configure.8.xml

clean:
	rm -f *.1 *.8

install:
	mkdir -m0755 -p $(DESTDIR)/$(BINDIR) $(DESTDIR)/$(SBINDIR) $(DESTDIR)/$(MANDIR)/man1 $(DESTDIR)/$(MANDIR)/man8 $(KEYSDIR)
	install -m 0755 dnskey-pull $(DESTDIR)/$(BINDIR)
	install -m 0755 dnssec-configure $(DESTDIR)/$(SBINDIR)
	install -m 0644 dnskey-pull.1 $(DESTDIR)/$(MANDIR)/man1/
	install -m 0644 dnssec-configure.8 $(DESTDIR)/$(MANDIR)/man8/
	cp -r production testing harvest dlv $(KEYSDIR)/
	@echo
	@echo "Run dnssec-configure to enable one or more Trusted Keys repositories and DNSSEC and/or DLV options."
	@echo


