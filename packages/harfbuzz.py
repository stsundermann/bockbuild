Package ('harfbuzz', '0.9.40',
	sources = ['http://www.freedesktop.org/software/%{name}/release/%{name}-%{version}.tar.bz2'],
	configure_flags = [
		'--disable-silent-rules',
		'--without-cairo',
		'--without-freetype',
		'--without-glib',
		'--without-graphite2',
		'--with-icu',
	])
