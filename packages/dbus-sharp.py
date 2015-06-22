class DbusSharpPackage (GitHubPackage):
	def __init__ (self):
		GitHubPackage.__init__ (self, 'mono', 'dbus-sharp', '0.7.0',
			revision = '60cd041dc9676161ed1dcce0652619cad3128159')

	def arch_build (self, arch):

		# Use mcs rather than gmcs
		self.sh ('sed -ie "s:GMCS, gmcs, no:GMCS, mcs, no:g" "configure.ac"')

		self.sh ('./autogen.sh --prefix="%{prefix}"')
		Package.arch_build (self, arch, defaults = False)

DbusSharpPackage ()
