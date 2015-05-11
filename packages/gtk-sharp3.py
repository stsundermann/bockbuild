class GtkSharp3Package (GitHubPackage):
	def __init__ (self):		
		GitHubPackage.__init__ (self, 'mono', 'gtk-sharp', '2.99.3.99',
			revision = 'a3db272fee017518779344293fb802cc8d1f813b')

		if Package.profile.name == 'darwin':
			self.sources.extend ([
				# Fix compilation on OS X
				# https://github.com/mono/gtk-sharp/pull/130
				'https://github.com/stsundermann/gtk-sharp/commit/af064c76266787bbbdd4309464d1bb4bb886e2ea.patch'
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
				self.sh ('./autogen.sh --prefix="%{prefix}"')
				Package.configure (self)
		elif arch == 'darwin-64':	
				self.local_ld_flags = ['-arch x86_64']
				self.local_gcc_flags = ['-arch x86_64']
				self.local_configure_flags.extend (['--build=x86_64-apple-darwin11.2.0'])
				self.sh ('./autogen.sh --prefix="%{prefix}"')
				Package.configure (self)
 
		Package.arch_build (self, arch, defaults = False)
 
GtkSharp3Package ()
