Package ('gnutls', '3.3.15', 
	sources = ['ftp://ftp.gnutls.org/gcrypt/%{name}/v3.3/%{name}-%{version}.tar.xz'],
	configure_flags = [
	'--disable-guile',
	'--disable-silent-rules',
	'--disable-libdane',
	'--with-p11-kit',
])
