class CmakePackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'cmake', '3.2.2', 
			sources = ['http://www.cmake.org/files/v3.2/%{name}-%{version}.tar.gz'])

		self.sources.extend ([
			'https://trac.macports.org/export/136239/trunk/dports/devel/cmake/files/macports.cmake',
			'https://trac.macports.org/export/136239/trunk/dports/devel/cmake/files/patch-CMakeFindFrameworks.cmake.diff',
			'https://trac.macports.org/export/136239/trunk/dports/devel/cmake/files/patch-Modules-FindFreetype.cmake.diff',
			'https://trac.macports.org/export/136239/trunk/dports/devel/cmake/files/patch-Modules-FindQt4.cmake.diff',
			'https://trac.macports.org/export/136239/trunk/dports/devel/cmake/files/patch-Modules-Platform-Darwin.cmake.diff',
			'https://trac.macports.org/export/136239/trunk/dports/devel/cmake/files/patch-Modules-Platform-Darwin-Initialize.cmake.diff',
			'https://trac.macports.org/export/136239/trunk/dports/devel/cmake/files/patch-Modules-noArchCheck.diff'
		])

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (2, len (self.sources)):
				self.sh ('patch -p0 --ignore-whitespace < "%{sources[' + str (p) + ']}"')
			self.sh ('cp %{sources[1]} .')
			self.sh ('sed -ie "s:__PREFIX__:%{prefix}:g" "macports.cmake"')
			self.sh ('sed -ie "s:__PREFIX__:%{prefix}:g" "Modules/CMakeFindFrameworks.cmake"')

	def build (self):
		self.sh (
			# Let's set a bunch of variables, to make cmake feel loved
			'CMAKE_PREFIX_PATH=%{prefix}',
			'CMAKE_INCLUDE_PATH=%{prefix}/include/ncurses',
			'CMAKE_LIBRARY_PATH=%{prefix}/lib',
			'CMAKE_INSTALL_PREFIX=%{prefix}',
			'CMAKE_OSX_SYSROOT=%s' % os.getenv('MACOSX_DEPLOYMENT_SDK_PATH'),
			# Currently the deployment target is hardcoded
			'CMAKE_OSX_DEPLOYMENT_TARGET=10.9',

			# and let's bootstrap
			'./bootstrap --init=macports.cmake --prefix=%{prefix} --docdir=share/doc/cmake --no-system-jsoncpp',

			# build and install
			'make; make install',
			)

CmakePackage ()
