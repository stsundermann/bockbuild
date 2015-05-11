class LibsoupPackage (GnomeXzPackage):
	def __init__ (self):
		GnomeXzPackage.__init__ (self, 'libsoup', '2.50', '0')
		self.configure_flags = [
			'--disable-gtk-doc',
			'--without-gnome'
		]

	def arch_build (self, arch):
		if arch == 'darwin-32':
				self.local_ld_flags = ['-arch i386']
				self.local_gcc_flags = ['-arch i386']
				self.local_configure_flags.extend (['--build=i386-apple-darwin11.2.0'])
				# The following will only work with bash according to:
				# http://www.gossamer-threads.com/lists/python/python/30602
				os.environ['VERSIONER_PYTHON_PREFER_32_BIT'] = 'yes'
		elif arch == 'darwin-64':
				self.local_ld_flags = ['-arch x86_64']
				self.local_gcc_flags = ['-arch x86_64']
				self.local_configure_flags.extend (['--build=x86_64-apple-darwin11.2.0'])

		Package.arch_build (self, arch, defaults = False)
		
LibsoupPackage ()
