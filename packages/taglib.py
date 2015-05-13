class TaglibPackage (GitHubPackage):
	def __init__ (self):		
		GitHubPackage.__init__ (self, 'taglib', 'taglib', '1.9.1.99',
			revision = '62ab41fa07bfe6456eafc7ffacbfa2043cba0668')

	def build (self):
		self.sh (
			# Let's set a bunch of variables, to make cmake feel loved
			'CMAKE_PREFIX_PATH=%{prefix}',
			'CMAKE_LIBRARY_PATH=%{prefix}/lib',
			'CMAKE_INSTALL_PREFIX=%{prefix}',

			# build and install
			'cmake -DCMAKE_INSTALL_PREFIX=%{prefix} . && make all install',
			)
 
TaglibPackage ()
