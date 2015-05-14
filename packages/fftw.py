class FftwPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'fftw', '3.3.4', 
			sources = ['http://www.fftw.org/%{name}-%{version}.tar.gz'],
			configure_flags = [
			'--enable-single',
			'--enable-shared',
			'--disable-doc',
			'--enable-threads',
			'--enable-sse',
			'--disable-dependency-tracking',
			])
 
	def arch_build (self, arch):

        # Building with --enable-debug causes issues when compiling for i386 on x86_64
		self.configure_flags.remove("--enable-debug")
		self.configure_flags.extend(['--disable-debug'])

		if arch == 'darwin-32':
			self.ld_flags = ['-arch i386']
			self.gcc_flags = ['-arch i386']
			self.local_configure_flags.extend (['--disable-avx', '--disable-sse2', '--build=i386-apple-darwin11.2.0'])
		elif arch == 'darwin-64':
			self.ld_flags = ['-arch x86_64']
			self.gcc_flags = ['-arch x86_64']
			self.local_configure_flags.extend (['--enable-avx', 'enable-sse2', '--build=x86_64-apple-darwin11.2.0'])

		Package.arch_build (self, arch, defaults = False)

FftwPackage ()
