class WavpackPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'wavpack', '4.70.0', sources = [
			'http://www.wavpack.com/%{name}-%{version}.tar.bz2'
		]) 

		self.sources.extend ([
				# define @exec_prefix@ in wavpack.pc to fix configuration
				'https://trac.macports.org/export/136232/trunk/dports/audio/wavpack/files/patch-wavpack.pc.in.diff'
				])

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (1, len (self.sources)):
				self.sh ('patch -p0 --ignore-whitespace < "%{sources[' + str (p) + ']}"')

WavpackPackage ()
