class GettextPackage (GnuPackage):
	def __init__ (self):
		GnuXzPackage.__init__ (self, 'gettext', '0.19.4',
			configure_flags = [
				'--disable-java',
				'--disable-libasprintf',
				'--disable-openmp'
			]
		)

		if Package.profile.name == 'darwin':
			self.configure_flags.extend ([
				# only build the tools, osx has the lib
				# https://github.com/mxcl/homebrew/blob/master/Library/Formula/gettext.rb
				#'--without-included-gettext',
			])
			self.sources.extend ([
				# Don't build samples
				# https://trac.macports.org/export/79183/trunk/dports/devel/gettext/files/patch-gettext-tools-Makefile.in
				'patches/gettext-no-samples.patch',
			])

		#This package would like to be built with fat binaries
		if Package.profile.m64 == True:
			self.fat_build = True

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (1, len (self.sources)):
				self.sh ('patch -p1 < "%{sources[' + str (p) + ']}"')

GettextPackage ()
