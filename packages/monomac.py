class MonoMacPackage (GitHubTarballPackage):
	def __init__ (self):
		self.pkgconfig_version = '1.0'
		self.maccore_tag = 'ef6a975'
		self.maccore_source_dir_name = 'mono-maccore-%{maccore_tag}'
		self.monomac_tag = '36508cf'
		self.monomac_source_dir_name = 'mono-monomac-%{monomac_tag}'
		
		Package.__init__ (self, 'monomac', self.monomac_tag)
		
		self.sources = ([
			'https://github.com/mono/monomac/tarball/%{monomac_tag}',
			'https://github.com/mono/maccore/tarball/%{maccore_tag}',
			])

	def prep (self):

		# Thank you for building MonoMac
		self.sh ('tar xf "%{sources[0]}"')
		self.sh ('tar xf "%{sources[1]}"')
		
		# Have you tried turning it off and on again?
		self.sh ('rm -rf monomac')
		
		# You build experience is important to us
		self.sh ('mv %{monomac_source_dir_name} monomac')
		
		# Please hold for frobnication of the pkg-config path
		self.sh ('sed -ie "s:/Library/Frameworks/Mono.framework/Commands/pkg-config:PKG_CONFIG=%{prefix}/bin/pkg-config:g" "monomac/src/Makefile"')

		# New packaging weight loss system, with zero dependencies on MonoDevelop.. you heard that right.. zero!
		self.sh ('sed -ie "s:DIRS = src samples:DIRS = src:g" "monomac/Makefile"')

		# You have been selected for a special upgrade, free maccore support
		self.sh ('rm -rf monomac/maccore')
		self.sh ('mv %{maccore_source_dir_name} monomac/maccore')

		# Thank you, your build is number 1 in the queue.
		self.cd ('monomac')
	
	def build (self):
		# If we are not building with Mono 2.11+, we are doing it wrong.
		self.sh ('HAVE_ASYNC=1 make')

	def install (self):
		self.sh ('mkdir -p %{prefix}/lib/monomac')
		self.sh ('mkdir -p %{prefix}/share/pkgconfig')
		self.sh ('echo "Libraries=%{prefix}/lib/monomac/MonoMac.dll\n\nName: MonoMac\nDescription: Mono Mac bindings\nVersion:%{pkgconfig_version}\nLibs: -r:%{prefix}/lib/monomac/MonoMac.dll" > %{prefix}/lib/pkgconfig/monomac.pc')
		self.sh ('cp src/MonoMac.dll %{prefix}/lib/monomac/')

MonoMacPackage ()
