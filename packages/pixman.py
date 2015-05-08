class PixmanPackage (CairoGraphicsPackage):
	def __init__ (self):
		CairoGraphicsPackage.__init__ (self, 'pixman', '0.32.6')
		
		#This package would like to be built with fat binaries
		if Package.profile.m64 == True:
			self.fat_build = True

PixmanPackage ()
