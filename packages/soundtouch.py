class SoundtouchPackage (Package):
	def __init__(self):
		Package.__init__ (self, 'soundtouch', '1.9.0',
			sources = [
				'http://www.surina.net/%{name}/%{name}-%{version}.tar.gz'
			],
			configure_flags = ['--disable-silent-rules', '--disable-static', '--enable-shared'],
			source_dir_name = "soundtouch"
		)

	def arch_build(self, arch):
		self.sh("./bootstrap")

		if arch == 'darwin-32':
			self.ld_flags = ['-arch i386']
			self.gcc_flags = ['-arch i386']
			self.configure = 'AM_CXXFLAGS="-arch i386" ./configure --prefix="%{package_prefix}"'
			self.local_configure_flags.extend (['--build=i386-apple-darwin11.2.0'])
		elif arch == 'darwin-64':
			self.ld_flags = ['-arch x86_64']
			self.gcc_flags = ['-arch x86_64']
			self.configure = 'AM_CXXFLAGS="-arch x86_64" ./configure --prefix="%{package_prefix}"'
			self.local_configure_flags.extend (['--build=x86_64-apple-darwin11.2.0'])

		Package.arch_build (self, arch, defaults = False)

SoundtouchPackage()