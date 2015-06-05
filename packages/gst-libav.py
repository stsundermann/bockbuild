class GstLibavPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'gst-libav', '1.4.5',
						  sources = ['http://gstreamer.freedesktop.org/src/gst-libav/gst-libav-%{version}.tar.xz'],
						  configure_flags = [
							  '--disable-gtk-doc',
							  '--prefix=%{prefix}'
							  ])

	def arch_build (self, arch):

		# Building with --enable-debug causes issues when compiling for i386 on x86_64
		self.configure_flags.remove("--enable-debug")
		self.configure_flags.extend(['--disable-debug'])

		if arch == 'darwin-32':
			self.ld_flags = ['-arch i386']
			self.gcc_flags = ['-arch i386']
			self.local_configure_flags.extend (['--disable-avx', '--disable-sse2', '--build=i686-apple-darwin11.2.0', '--host=i686-apple-darwin11.2.0'])
		elif arch == 'darwin-64':
			self.ld_flags = ['-arch x86_64']
			self.gcc_flags = ['-arch x86_64']
			self.local_configure_flags.extend (['--enable-avx', 'enable-sse2', '--build=x86_64-apple-darwin11.2.0', '--host=x86_64-apple-darwin11.2.0'])

		Package.arch_build (self, arch, defaults = False)

GstLibavPackage ()
