class DbusSharpPackage (GitHubPackage):
	def __init__ (self):		
		GitHubPackage.__init__ (self, 'mono', 'dbus-sharp', '0.8.99',
			revision = 'fb3dd1221fb5dceb4c07d7747f638d940680e63f')

	def arch_build (self, arch):

		# Use mcs rather than gmcs
		self.sh ('sed -ie "s:GMCS, gmcs, no:GMCS, mcs, no:g" "configure.ac"')
		
		self.sh ('./autogen.sh --prefix="%{prefix}"')
		Package.arch_build (self, arch, defaults = False)

DbusSharpPackage ()
