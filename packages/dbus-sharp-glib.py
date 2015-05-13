class DbusSharpGlibPackage (GitHubPackage):
	def __init__ (self):		
		GitHubPackage.__init__ (self, 'mono', 'dbus-sharp-glib', '0.5.0.1',
			revision = 'eeccd9126d050c0537be64530a933adefe2ee5a6')

	def arch_build (self, arch):
		self.sh ('sed -ie "s:GMCS, gmcs, no:GMCS, mcs, no:g" "configure.ac"')
		self.sh ('./autogen.sh --prefix="%{prefix}"')
		Package.arch_build (self, arch, defaults = False)
 
DbusSharpGlibPackage ()
