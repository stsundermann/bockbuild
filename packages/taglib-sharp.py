class TaglibSharpPackage (GitHubPackage):
	def __init__ (self):		
		GitHubPackage.__init__ (self, 'mono', 'taglib-sharp', '2.1.0.1',
			revision = 'a5f6949a53d09ce63ee7495580d6802921a21f14',
			configure_flags = ['--disable-docs'])

	def arch_build (self, arch):

		# Use mcs rather than gmcs
		self.sh ('sed -ie "s:MCS, gmcs:MCS, mcs:g" "configure.ac"')

		self.sh ('./autogen.sh --disable-docs --prefix="%{prefix}"')
		Package.arch_build (self, arch, defaults = False)

TaglibSharpPackage ()
