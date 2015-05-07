class GtkPackage (GnomeXzPackage):
	def __init__ (self):
		GnomeXzPackage.__init__ (self, 'gtk+', version_major = '3.16', version_minor = '2',
			configure_flags = [
				'--with-gdktarget=quartz',
				'--enable-quartz-backend',
				'--enable-debug',
				'--enable-static',
				'--disable-glibtest',
				'--enable-introspection',
				'--disable-cloudprint',
				'--disable-wayland-backend',
				'--disable-schemas-compile',
				'gio_can_sniff=yes'
			]
		)
		self.gdk_target = 'quartz'
 
		if Package.profile.name == 'darwin':
			self.gdk_target = 'quartz'
			self.sources.extend ([
				# Custom gtkrc
				'patches/gtkrc'
			])
 
		if Package.profile.name == 'darwin' and not Package.profile.m64:
			self.configure_flags.extend ([
				# fix build on lion, it uses 64-bit host even with -m32
				'--build=i386-apple-darwin11.2.0',
			])
 
 
	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (2, len (self.sources)):
				self.sh ('patch -p1 --ignore-whitespace < "%{sources[' + str (p) + ']}"')
 
	def arch_build (self, arch):
 
		if arch == 'darwin-32':
				self.sh ('export CC="$CC -arch i386"')
				self.sh ('export CXX="$CXX -arch i386"')
				self.local_ld_flags = ['-arch i386', '-DX_LOCALE']
				self.local_gcc_flags = ['-arch i386', '-fstrict-aliasing']
				# The following will only work with bash according to:
				# http://www.gossamer-threads.com/lists/python/python/30602
				os.environ['VERSIONER_PYTHON_PREFER_32_BIT'] = 'yes'
		elif arch == 'darwin-64':
				self.sh ('export CC="$CC -arch x86_64"')
				self.sh ('export CXX="$CXX -arch x86_64"')
				self.local_ld_flags = ['-arch x86_64', '-DX_LOCALE']
				self.local_gcc_flags = ['-arch x86_64', '-fstrict-aliasing']
 
		Package.arch_build (self, arch, defaults = False)
 
	def install(self):
		Package.install(self)
		if Package.profile.name == 'darwin':
			self.install_gtkrc ()
 
	def install_gtkrc(self):
		gtkrc = self.sources[1]
		origin = gtkrc if os.path.isabs (gtkrc) else os.path.join (self.package_dir (), gtkrc)
		destdir = os.path.join (self.prefix, "etc", "gtk-2.0")
		if not os.path.exists (destdir):
			os.makedirs(destdir)
		self.sh('cp %s %s' % (origin, destdir))
 
GtkPackage ()
