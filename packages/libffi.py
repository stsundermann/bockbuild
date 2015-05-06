class LibFfiPackage (Package):
	def __init__ (self):		
		Package.__init__ (self, 'libffi', '3.2.1', sources = [
		'ftp://sourceware.org/pub/%{name}/%{name}-%{version}.tar.gz'])

		if Package.profile.name == 'darwin':
			self.sources.extend ([
				'https://trac.macports.org/export/135853/trunk/dports/devel/libffi/files/PR-44170.patch'
			])
				
		#This package would like to be built with fat binaries
		if Package.profile.m64 == True:
			self.fat_build = True

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (1, len (self.sources)):
				self.sh ('patch -p0 --ignore-whitespace < "%{sources[' + str (p) + ']}"')

LibFfiPackage ()