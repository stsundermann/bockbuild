class LibGcryptPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'libgcrypt', '1.6.3',
                                  configure_flags = [ '--disable-asm' ], sources = [
	'ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2'
                                  ])

LibGcryptPackage ()
