class LibGlade3Package (GnomeXzPackage):
	def __init__ (self):		
		GnomeXzPackage.__init__ (self, 'glade', version_major = '3.18', version_minor = '3',
			configure_flags = ['--disable-debug', '--disable-scrollkeeper', '--disable-gnome', '--disable-python', '--disable-docs', '--disable-gtk-doc'])

		self.sources.extend ([
		# Fixes from upstream via MacPorts
		'https://trac.macports.org/export/136311/trunk/dports/devel/glade/files/patch-upstream-fixes-thru-20141205.diff'
		])

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (1, len (self.sources)):
				self.sh ('patch -p0 --ignore-whitespace < "%{sources[' + str (p) + ']}"')

	def arch_build (self, arch):

		# reconfigure using upstream autogen.sh for intltool 0.51 compatibility
		# This requires the gnome-common package.
		# Once package is updated to 3.18.3+ when this is no longer required
		# please remember to remove gnome-common from the dependency list.
		self.sh ('./autogen.sh --disable-python --disable-gnome --disable-docs --disable-scrollkeeper --prefix="%{prefix}"')

		
		# disable optimization which (at least with clang)
		# causes glade to segfault on startup
		# after displaying main window

		self.local_gcc_flags = ['-O0', '-Wno-format-nonliteral']
		
		Package.arch_build (self, arch, defaults = False)

LibGlade3Package ()
