class LibPngPackage (SourceForgeXzPackage):
	def __init__ (self):
		SourceForgeXzPackage.__init__ (self, 'libpng', 'libpng', '1.6.17', configure_flags = ['--enable-shared'])

		# If we are on OS X this package likes to be a fat binary
		if Package.profile.name == 'darwin':
			if Package.profile.m64 == True:
				self.fat_build = True

LibPngPackage()