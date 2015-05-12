class GlibPackage (GnomeXzPackage):
	def __init__ (self):
		GnomeXzPackage.__init__ (self,
			'glib',
			version_major = '2.44',
			version_minor = '0')

		self.darwin = Package.profile.name == 'darwin'

		if Package.profile.name == 'darwin':
			
			# 05.05.15: Patches from MacPorts to compile glib 2.44.0 on OS X, excluding patches which redefine paths for MacPorts' build system
			# See: https://trac.macports.org/browser/trunk/dports/devel/glib2/Portfile

			self.sources.extend ([
				'https://trac.macports.org/export/135842/trunk/dports/devel/glib2/files/config.h.ed',
				'https://trac.macports.org/export/135842/trunk/dports/devel/glib2/files/patch-configure.diff',
				'https://trac.macports.org/export/135842/trunk/dports/devel/glib2/files/patch-glib-2.0.pc.in.diff',
				'https://trac.macports.org/export/135842/trunk/dports/devel/glib2/files/patch-glib-gmain.c.diff',
				'https://trac.macports.org/export/135842/trunk/dports/devel/glib2/files/patch-glib_gunicollate.c.diff',
				'https://trac.macports.org/export/135842/trunk/dports/devel/glib2/files/patch-gi18n.h.diff',
				'https://trac.macports.org/export/135842/trunk/dports/devel/glib2/files/patch-get-launchd-dbus-session-address.diff',
				'https://trac.macports.org/export/135860/trunk/dports/devel/glib2/files/patch-gio-giotypes.h.diff',
				'https://trac.macports.org/export/135842/trunk/dports/devel/glib2/files/patch-gmodule-gmodule-dl.c.diff'
			])
			
		if Package.profile.name == 'darwin' and not Package.profile.m64:
			self.configure_flags.extend ([
				# fix building i386 on x86_64
                '--build=i386-apple-darwin11.2.0',
			])

	def prep (self):
		Package.prep (self)
		if self.darwin:
			for p in range (2, len (self.sources)):
				self.sh ('patch --ignore-whitespace -p0 < %{sources[' + str (p) + ']}')

	def arch_build (self, arch):

		if arch == 'darwin-fat': #multi-arch  build pass
			self.local_ld_flags = ['-arch i386' , '-arch x86_64', '-lresolv', '-bind_at_load']
			self.local_gcc_flags = ['-arch i386' , '-arch x86_64', '-Os', '-fstrict-aliasing']
		elif arch == 'darwin-32':
				self.local_ld_flags = ['-arch i386', '-lresolv', '-bind_at_load']
				self.local_gcc_flags = ['-arch i386', '-fstrict-aliasing']
		elif arch == 'darwin-64':
				self.local_ld_flags = ['-arch x86_64', '-lresolv', '-bind_at_load']
				self.local_gcc_flags = ['-arch x86_64', '-fstrict-aliasing']

		#modified build for darwin
		if arch.startswith ('darwin'): 
			self.local_configure_flags.extend (['--disable-compile-warnings', '--enable-static', '--disable-libelf', '--disable-dependency-tracking', '--disable-dtrace'])
			Package.configure (self)
			self.sh (
				# 'autoconf',
				#'%{configure} --disable-compile-warnings',
				'ed - config.h < %{sources[1]}',
				# work around https://bugzilla.gnome.org/show_bug.cgi?id=700350
				'touch docs/reference/*/Makefile.in',
				'touch docs/reference/*/*/Makefile.in',
				#'%{make}'
			)
			Package.make (self)
		else:	
			Package.arch_build (self, arch, defaults = False)
	
	def install (self):
		Package.install (self)
		if self.darwin:
			# FIXME: necessary?
			self.sh ('rm -f %{prefix}/lib/charset.alias')

GlibPackage ()
