class LibepoxyPackage (GitHubPackage):
	def __init__ (self):		
		GitHubPackage.__init__ (self, 'anholt', 'libepoxy', '1',
			revision = '20062c25e7612cab023cdef44d3277ba1bd0b2de',
			configure = './autogen.sh --prefix="%{prefix}"'
			)
 
	def arch_build (self, arch):
 
		if arch == 'darwin-32':
				self.local_ld_flags = ['-arch i386']
				self.local_gcc_flags = ['-arch i386']
				self.local_configure_flags.extend (['--build=i386-apple-darwin11.2.0'])
		elif arch == 'darwin-64':	
				self.local_ld_flags = ['-arch x86_64']
				self.local_gcc_flags = ['-arch x86_64']
				self.local_configure_flags.extend (['--build=x86_64-apple-darwin11.2.0'])
 
		Package.arch_build (self, arch, defaults = False)
 
LibepoxyPackage ()
