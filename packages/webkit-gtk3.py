class WebkitPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'webkitgtk', '2.9.1',
			sources = ['http://webkitgtk.org/releases/%{name}-%{version}.tar.xz'],
			configure_flags = [
				'--disable-video',
				'--disable-geolocation',
				'--disable-xslt',
			]
		)

		if Package.profile.name == 'darwin':
			self.configure_flags.extend ([
				'--with-target=quartz',
				'--with-gtk=3.0',
				'--disable-gtk-doc'
			])

			# self.sources.extend ([])

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (1, len (self.sources)):
				self.sh ('patch -p0 < "%{sources[' + str (p) + ']}"')

	def build (self):
		self.sh (
			# Let's set a bunch of variables, to make cmake feel loved
			'CMAKE_PREFIX_PATH=%{prefix}',
			'CMAKE_LIBRARY_PATH=%{prefix}/lib',
			'CMAKE_INSTALL_PREFIX=%{prefix}',

			# build and install
			'cmake -DCMAKE_SYSTEM_PROCESSOR=i386 -DPORT=GTK -DCMAKE_INSTALL_PREFIX=%{prefix} . && make all install',
			)

WebkitPackage()
