GitHubPackage ('mono', 'libgdiplus', '3.12',
	revision = 'f18514c8babf20301f8bbd1f0cfd587ed48a480b',
	configure = 'CFLAGS="%{gcc_flags} %{local_gcc_flags} -I/opt/X11/include" ./autogen.sh --prefix="%{package_prefix}"', 
	override_properties = { 'make': 'C_INCLUDE_PATH="" make' })
