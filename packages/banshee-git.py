GnomeGitPackage ('banshee', '2.99', 
	override_properties = { 'configure': 'NOCONFIGURE=1 ./autogen.sh && ./profile-configure %{profile.name} --prefix=%{prefix}'})
