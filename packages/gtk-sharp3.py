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

		if Package.profile.name == 'darwin' and not Package.profile.m64:
			self.configure_flags.extend ([
				# fix building i386 on x86_64
                '--build=i386-apple-darwin11.2.0',
			])

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (1, len (self.sources)):
				self.sh ('patch -p1 --ignore-whitespace < "%{sources[' + str (p) + ']}"')
				
		# Run autogen, the correct flags will be picked automatically up when configure is run.
		self.sh ('./autogen.sh --prefix="%{prefix}"')

GtkSharp3Package ()
