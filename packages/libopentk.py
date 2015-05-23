class OpenTKPackage (GitHubPackage):
	def __init__ (self):		
		GitHubPackage.__init__ (self, 'opentk', 'opentk', '1.1.4.1',
			revision = '788b039e325b23575d6e8ed652a802446d1ea06e',
			override_properties = {
			'configure': 'echo empty',
			'make': 'xbuild  /p:Configuration=Release OpenTK.sln'}
			)

	def install (self):
		self.sh (
			'mkdir -p %{prefix}/lib/mono/opentk/',
			'cp Source/OpenTK/obj/Release/OpenTK.dll %{prefix}/lib/mono/opentk/',
			'cp Source/OpenTK/obj/Release/OpenTK.OpenTK.dll.config %{prefix}/lib/mono/opentk/',
			'gacutil -i %{prefix}/lib/mono/opentk/OpenTK.dll -package OpenTK')

OpenTKPackage ()
