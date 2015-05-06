class CairoPackage (CairoGraphicsXzPackage):
	def __init__ (self):
		CairoGraphicsXzPackage.__init__ (self, 'cairo', '1.14.2')

		#This package would like to be built with fat binaries
		# if Package.profile.m64 == True:
		# 	self.fat_build = True

	def build (self):

		if Package.profile.name == 'darwin':
			self.configure_flags.extend ([
				'--disable-gl',
				'--enable-quartz',
				'--enable-quartz-font',
				'--enable-quartz-image',
				'--disable-silent-rules',
				'--disable-symbol-lookup',
				'--disable-xlib',
				'--disable-xlib-xcb',
				'--disable-xcb',
				'--disable-xcb-shm',
				'--without-x',
				'--enable-ft',
				'--enable-pdf',
				'--enable-png',
				'--enable-ps',
				'--enable-script',
				'--enable-svg',
				'--enable-tee',
				'--enable-xml'				
			])
		elif Package.profile.name == 'linux':
			self.configure_flags.extend ([
				'--disable-quartz',
				'--with-x'
			])

		Package.build (self)

CairoPackage ()
