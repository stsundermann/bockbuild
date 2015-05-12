class LibTheoraPackage (XiphPackage):
	def __init__ (self):
		XiphPackage.__init__ (self, 'theora', 'libtheora', '1.1.1',
			configure_flags = [
				'--disable-docs',
				'--disable-oggtest',
				'--disable-vorbistest',
				'--disable-example',
				'--disable-asm'
			])

		if Package.profile.name == 'darwin':
			self.sources.extend ([
				# Fix building with libpng 1.6+
				'https://git.xiph.org/?p=mirrors/theora.git;a=patch;h=4bedff504fbc8714264c15dc69559f9a3d0a4a22;hp=b477a643d80871ec1171a85887140cd154c78455',
				# Patch from MacPorts to fix compilation with some versions of xcode's clang
				'https://trac.macports.org/export/136143/trunk/dports/multimedia/libtheora/files/patch-configure.diff'
				])

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			self.sh ('patch -p1 --ignore-whitespace < "%{sources[1]}"')
			for p in range (2, len (self.sources)):
				self.sh ('patch -p0 --ignore-whitespace < "%{sources[' + str (p) + ']}"')

LibTheoraPackage ()
