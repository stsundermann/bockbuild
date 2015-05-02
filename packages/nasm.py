class NasmPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'nasm', '2.11.08', sources = [
			'http://www.nasm.us/pub/nasm/releasebuilds/%{version}/nasm-%{version}.tar.xz'
		])

NasmPackage ()
