GnomeGitPackage ('banshee', '2.99', 
	revision = '5638d304a328f92b516e0543994504b2140be8de',
	override_properties = { 'configure': 'NOCONFIGURE=1 ./autogen.sh && ./profile-configure %{profile.name} --prefix=%{prefix}'})
