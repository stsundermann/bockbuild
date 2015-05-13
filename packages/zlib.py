class ZlibPackage (Package):
	def __init__ (self):		
		Package.__init__ (self, 'zlib', '1.2.8', 
			sources = ['http://zlib.net/%{name}-%{version}.tar.gz'])

		self.sources.extend ([
		# Fix configuration when using clang
		'https://trac.macports.org/export/136252/trunk/dports/archivers/zlib/files/patch-configure-clang.diff'
		])
		
	def prep (self):
		Package.prep (self)
		for p in range (1, len (self.sources)):
			self.sh ('patch -p1 --ignore-whitespace < "%{sources[' + str (p) + ']}"')

	def arch_build (self, arch):
		# zlib fails on configure if --enable-debug is present in configure_flags
		self.configure_flags.remove("--enable-debug")

		Package.arch_build (self, arch, defaults = False)

ZlibPackage ()
