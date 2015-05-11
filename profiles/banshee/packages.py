import os
from bockbuild.darwinprofile import DarwinProfile
from bockbuild.gnomeprofile import GnomeProfile
from bockbuild.glickprofile import GlickProfile

class BansheePackages:
	def __init__ (self):
		# Toolchain
		self.packages.extend ([
			'autoconf.py',
			'automake.py',
			'tar.py',
			'xz.py',
			'libtool.py',
			'gettext.py',
			'pkg-config.py',
		])

		# Base Libraries
		self.packages.extend ([
			'libpng.py',
			'libjpeg.py',
			'libxml2.py',
			'libffi.py',
			'libtiff.py',
			'freetype.py',
			'fontconfig.py',
			'pixman.py',
			'glib.py',
			'gobject-introspection.py',
			'libcroco.py',
			'cairo.py',
			'pango.py',
			'atk.py',
			'intltool.py',
			'gdk-pixbuf.py',
			'util-macros.py',
			'libepoxy.py',
			'cairo.py',
			'gtk+3.py',
			# 'gconf-dummy.py',
			'libgpg-error.py',
			'libgcrypt.py',
			'gmp.py',
			'nettle.py',
			'gnutls.py',
			'intltool.py',
			'glib-networking.py',
			'sqlite.py',
			'libsoup.py',
		])

		# banshee-community-extensions
		self.packages.extend ([
			# lastfm fingerprint
			'fftw.py',
			'libsamplerate.py',

			# openvp (currently not working)
			#'libopentk.py',
			'libsdl.py',
			'libglade.py',

		])

		# exclude package with possible patent/copyright issues
		# when doing release builds
		if not self.cmd_options.release_build:
			self.packages.extend ([
				# BCE streamrecorder
				'lame.py',
			])

		# WebKit-gtk
		# TODO on darwin currently fails on the build stage
		# so don't include it on darwin for now
		if not isinstance (self, DarwinProfile):
			self.packages.extend ([
		# WebKit-gtk dependencies
				'gperf.py',
				'enchant.py',
				'libicu.py',
				'zlib.py',
				'webkit.py'
			])

		# Theme
		self.packages.extend ([
			'librsvg.py',
			'icon-naming-utils.py',
			'hicolor-icon-theme.py',
			'tango-icon-theme.py',
			'murrine.py'
		])

		# Codecs
		self.packages.extend ([
			'libogg.py',
			'libvorbis.py',
			'flac.py',
			'libtheora.py',
			'speex.py',
			'wavpack.py',
			'taglib.py',
		])

		# GStreamer
		self.packages.extend ([
			'liboil.py',
			'gstreamer.py',
			'gst-plugins-base.py',
			'gst-plugins-good.py'
		])

		if isinstance (self, DarwinProfile):
			self.packages.extend ([
				'gst-plugins-bad.py',
				'gst-plugins-ugly.py'
			])

		# Mono
		self.packages.extend ([
			'mono.py',
			'gtk-sharp3.py',
			'mono-addins.py',
			'dbus-sharp.py',
			'dbus-sharp-glib.py',
			'taglib-sharp.py',
			'mono-upnp.py',
		])

		if isinstance (self, DarwinProfile):
			self.packages.extend ([
				'monomac.py',
				'gtk-mac-integration.py'
			])

		if self.cmd_options.release_build:
			self.packages.append ('banshee-git.py')

		self.packages = [os.path.join ('..', '..', 'packages', p)
			for p in self.packages]
