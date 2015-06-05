class YasmPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'yasm', '1.3.0', sources = [
			'http://www.tortall.net/projects/yasm/releases/yasm-%{version}.tar.gz'
		])

YasmPackage ()
