# A bit overkill, but rpm does not like redirecting output?
#

all:	production.conf testing.conf

production.conf:
	cat production/*.conf > production.conf

testing.conf:
	cat testing/*.conf > testing.conf

clean:
	rm -f production.conf testing.conf harvest/*.conf

install:
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
	@echo "			trusted-keys-file: \"/var/lib/unbound/production.conf\"";


