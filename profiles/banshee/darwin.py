#!/usr/bin/python -B

import os
import sys

sys.path.append ('../..')

from bockbuild.darwinprofile import DarwinProfile
from packages import BansheePackages

class BansheeDarwinProfile (DarwinProfile, BansheePackages):
	def __init__ (self):
		DarwinProfile.__init__ (self, min_version = 9)
		BansheePackages.__init__ (self)

		self_dir = os.path.realpath (os.path.dirname (sys.argv[0]))
		self.bundle_skeleton_dir = os.path.join (self_dir, 'skeleton.darwin')
		self.bundle_output_dir = os.path.join (self_dir, 'bundle.darwin')

		self.bundle_from_build = [
			'bin/mono',
			'lib/mono/2.0/gmcs.exe',
			'lib/mono/gac/Mono.Addins.CecilReflector',
			'bin/banshee',
			'lib/banshee',
			'lib/pango',
			'lib/gtk-2.0/2.10.0/loaders',
			'lib/gtk-2.0/2.10.0/engines',
			'lib/gtk-2.0/2.10.0/immodules',
			'lib/gdk-pixbuf-2.0/2.10.0/loaders',
			'lib/gstreamer-0.10',
			'share/banshee',
			'share/locale',
			'etc/mono/config',
			'etc/mono/1.0/machine.config',
			'etc/mono/2.0/machine.config',
			'etc/mono/2.0/settings.map',
			'share/icons/hicolor/index.theme',
			'share/icons/Tango/index.theme'
		]

		self.bundle_from_build.extend ([
			'share/icons/%s/%sx%s' % (theme, size, size)
				for size in [16, 22, 32, 48]
				for theme in ['hicolor', 'Tango']
		])

		self.env.set('MONO_GAC_PREFIX', self.prefix)
		self.env.set('MONO_INSTALL_PREFIX', self.prefix)
		self.env.set('MONO_ADDINS_REGISTRY', self.prefix + '/addinreg')
		self.env.set('DYLD_FALLBACK_LIBRARY_PATH', self.prefix + '/lib:/lib:/usr/lib')

	def bundle (self):
		banshee_path = os.path.join (self.prefix, 'lib', 'banshee')
		os.environ['MONO_PATH'] = ':'.join ([
			banshee_path,
			os.path.join (banshee_path, 'Extensions'),
			os.path.join (banshee_path, 'Backends')
		])

		DarwinProfile.bundle (self)

		import shutil
		import glob

		bin_path = os.path.join (self.bundle_macos_dir, 'Banshee')
		shutil.move (os.path.join (self.bundle_res_dir, 'bin', 'banshee'), bin_path)
		os.chmod (bin_path, 0755)

		for nuke in [ 'NotificationArea', 'AudioCd', 'MiniMode' ]:
			for path in glob.glob (os.path.join (self.bundle_res_dir,
				'lib', 'banshee', 'Extensions', 'Banshee.%s*' % nuke)):
				os.unlink (path)

BansheeDarwinProfile ().build ()
