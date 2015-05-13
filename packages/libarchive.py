Package ('libarchive', '3.1.2', sources = ['http://libarchive.org/downloads/%{name}-%{version}.tar.gz'],
	configure_flags = [
	'--enable-bsdtar=shared',
	'--enable-bsdcpio=shared',
	'--disable-silent-rules',
	'--without-nettle']
)
