class SoundtouchPackage (Package):
	def __init__(self):
		Package.__init__ (self, 'soundtouch', '1.9.0',
			sources = [
				'http://www.surina.net/%{name}/%{name}-%{version}.tar.gz'
			],
			source_dir_name = "soundtouch",
			override_properties = {'configure': './bootstrap && ./configure --prefix="%{package_prefix}"'}
		)

	def arch_build(self, arch):
		# Building with --enable-debug causes issues when compiling for i386 on x86_64
		self.configure_flags.remove("--enable-debug")
		self.configure_flags.extend(['--disable-debug'])

		if arch == 'darwin-32':
			self.ld_flags = ['-arch i386']
			self.gcc_flags = ['-arch i386']
			self.local_configure_flags.extend (['--build=i386-apple-darwin11.2.0'])
		elif arch == 'darwin-64':
			self.ld_flags = ['-arch x86_64']
			self.gcc_flags = ['-arch x86_64']
			self.local_configure_flags.extend (['--build=x86_64-apple-darwin11.2.0'])

		Package.arch_build (self, arch, defaults = False)

SoundtouchPackage()