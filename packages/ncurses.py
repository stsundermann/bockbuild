class NcursesPackage (GnuPackage):
	def __init__ (self):
		GnuPackage.__init__ (self, 'ncurses', '5.9')
		

		self.sources.extend ([
				'https://trac.macports.org/export/136235/trunk/dports/devel/ncurses/files/hex.diff',
				'https://trac.macports.org/export/136235/trunk/dports/devel/ncurses/files/ungetch_guard.diff',
				'https://trac.macports.org/export/136235/trunk/dports/devel/ncurses/files/configure.diff',
				'https://trac.macports.org/export/136235/trunk/dports/devel/ncurses/files/constructor_types.diff',
				'https://trac.macports.org/export/136235/trunk/dports/devel/ncurses/files/pkg_config_libdir.diff'
		])

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (1, len (self.sources)):
				self.sh ('patch -p0 --ignore-whitespace < "%{sources[' + str (p) + ']}"')


	def make (self):
		self.local_make_flags.extend (['-DPKG_CONFIG_LIBDIR=%s' % self.PKG_CONFIG_PATH]) 
		Package.make (self)

NcursesPackage ()
