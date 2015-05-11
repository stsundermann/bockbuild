class FlacPackage (XiphXzPackage):
	def __init__ (self):
		XiphXzPackage.__init__ (self, 'flac', 'flac', '1.3.1',
			configure_flags = [
				'--disable-cpplibs',
				'--disable-silent-rules',
				'--disable-xmms-plugin'
			])

		if Package.profile.name == 'darwin':
			self.sources.extend ([
				# A couple of patches from MacPorts
				'https://trac.macports.org/export/136132/trunk/dports/audio/flac/files/patch-nasm.h.diff',
				'https://trac.macports.org/export/136132/trunk/dports/audio/flac/files/patch-build_lib.mk.diff',
				'https://trac.macports.org/export/136132/trunk/dports/audio/flac/files/autoconf-no-xmms.patch',
				'https://trac.macports.org/export/136132/trunk/dports/audio/flac/files/autoconf-cflags.patch'
				])

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (1, len (self.sources)):
				self.sh ('patch -p0 --ignore-whitespace < "%{sources[' + str (p) + ']}"')

		if Package.profile.name == 'darwin' and not Package.profile.m64:
			# disable asm optimizations on when compiling for i386
			self.configure_flags.append ('--disable-asm-optimizations')

		self.local_gcc_flags = ['-std=gnu89']

FlacPackage ()
