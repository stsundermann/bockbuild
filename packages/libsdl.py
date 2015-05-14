class LibSDLPackage (Package):
	def __init__ (self):		
		Package.__init__ (self, 'SDL', '1.2.15',
			sources = ['http://www.libsdl.org/release/%{name}-%{version}.tar.gz'])

		if Package.profile.name == 'darwin':
			self.configure_flags.extend ([
				# on OS X, compile without support for X.org
				'--without-x',
				])

			self.sources.extend ([
				# Fix for a bug preventing SDL from building at on OSX 10.9+
				# https://bugzilla.libsdl.org/show_bug.cgi?id=2085
				'patches/libSDL-compile-fix.patch'])

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (1, len (self.sources)):
				self.sh ('patch -p1 --ignore-whitespace < "%{sources[' + str (p) + ']}"')

LibSDLPackage ()
