class GmpPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'gmp', '6.0.0a', sources = [
			'https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz' ],
		configure_flags = ['--enable-cxx', '--disable-dependency-tracking']
		)
 
		self.source_dir_name = 'gmp-6.0.0'

	def arch_build (self, arch):
		if arch == 'darwin-32':
				self.local_ld_flags = ['-arch i386']
				self.local_gcc_flags = ['-arch i386']
				self.configure_flags.extend (['ABI=32'])
		if arch == 'darwin-64':
				self.local_ld_flags = ['-arch x86_64']
				self.local_gcc_flags = ['-arch x86_64']
				self.configure_flags.extend (['ABI=64'])

		Package.arch_build (self, arch, defaults = False)

GmpPackage ()
