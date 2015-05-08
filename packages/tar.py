class TarPackage (GnuXzPackage):
	def __init__ (self):
		GnuXzPackage.__init__ (self, 'tar', '1.28', configure_flags = ['--enable-nls=no'])

		if Package.profile.name == 'darwin':
			self.sources.extend ([
				# Fix build on OS X
				# https://lists.gnu.org/archive/html/bug-tar/2014-08/msg00001.html
				'patches/tar-xattrs-fix-bug-in-configure.patch'
			])

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (1, len (self.sources)):
				self.sh ('patch -p1 --ignore-whitespace < "%{sources[' + str (p) + ']}"')

		# Once tar-xattrs-fix-bug-in-configure.patch is in an upstream release this can go away
		# Until then tar must be placed after autoconf and automake in your packages file or your build will fail
		self.sh ('autoreconf')

TarPackage ()
