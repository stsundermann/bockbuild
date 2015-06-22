class DbusSharpGlibPackage (GitHubPackage):
	def __init__ (self):
		GitHubPackage.__init__ (self, 'mono', 'dbus-sharp-glib', '0.5.0',
			revision = '7a2e676e867fec8db6185334d4242ec440895c27')

	def arch_build (self, arch):
		self.sh ('sed -ie "s:GMCS, gmcs, no:GMCS, mcs, no:g" "configure.ac"')
		self.sh ('./autogen.sh --prefix="%{prefix}"')
		Package.arch_build (self, arch, defaults = False)

DbusSharpGlibPackage ()
