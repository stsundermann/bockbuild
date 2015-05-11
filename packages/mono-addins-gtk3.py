class MonoAddinsGTK3Package (GitHubPackage):
	def __init__ (self):		
		GitHubPackage.__init__ (self, 'mono', 'mono-addins', '0.6.2',
			revision = 'fbe9f412705aa2f4adb0aafc56fcb15671f36fbe',
			configure_flags = [
			'--disable-docs',
			# disable gtk#2 and enable gtk#3
			'--disable-gui',
			'--enable-gui-gtk3'
			])

	def prep (self):
		Package.prep (self)
		# Force use of mcs instead of gmcs
		self.sh ('sed -ie "s/gmcs/mcs/g" "configure.ac"')
		# Run autogen, initially disabling gtk#2 
		self.sh ('./autogen.sh --prefix="%{prefix}" --disable-gui')
 
MonoAddinsGTK3Package ()