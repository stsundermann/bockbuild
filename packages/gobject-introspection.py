class GObjectIntrospectionPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'gobject-introspection', '1.44.0', sources = ['https://download.gnome.org/sources/%{name}/1.44/%{name}-%{version}.tar.xz'], configure_flags = ['--disable-tests'])

		if Package.profile.name == 'darwin':
			self.sources.extend ([
				# A couple of patches from git post 1.44, can be removed when package is updated to 1.44.0+
				'https://git.gnome.org/browse/gobject-introspection/patch/?id=2699b11503550bcfde7a31bf867e4cf780d3d5f9',
				'https://git.gnome.org/browse/gobject-introspection/patch/?id=92d9c387687cf71f7113df54f0297fb0633c9afc',
				'https://git.gnome.org/browse/gobject-introspection/patch/?id=1f3db7840a2551a55c198f8b42ee6947f48b021e',
				'https://git.gnome.org/browse/gobject-introspection/patch/?id=90f69635057171b45cccb785fc1c53ccc992e0c3',
				'https://git.gnome.org/browse/gobject-introspection/patch/?id=cc6ef77db3dabae8ac56922e47fcfa39c599868b'
			])

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (1, len (self.sources)):
				self.sh ('patch -p1 --ignore-whitespace < "%{sources[' + str (p) + ']}"')

	def arch_build (self, arch):
		if arch == 'darwin-32':
				self.local_ld_flags = ['-arch i386']
				self.local_gcc_flags = ['-arch i386']
				self.local_configure_flags.extend (['--build=i386-apple-darwin11.2.0'])
				# The following will only work with bash according to:
				# http://www.gossamer-threads.com/lists/python/python/30602
				self.local_make_flags = ['VERSIONER_PYTHON_PREFER_32_BIT=yes']
				self.local_install_flags = ['VERSIONER_PYTHON_PREFER_32_BIT=yes']
		elif arch == 'darwin-64':
				self.local_ld_flags = ['-arch x86_64']
				self.local_gcc_flags = ['-arch x86_64']
				self.local_configure_flags.extend (['--build=x86_64-apple-darwin11.2.0'])

		Package.arch_build (self, arch, defaults = False)

GObjectIntrospectionPackage ()

