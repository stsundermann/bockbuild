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
			'zlib.py',
			'libtool.py',
			'gettext.py',
			'pkg-config.py',
			'libarchive.py',
			'ncurses.py',
			'cmake.py',
			'bison.py',
			'gnome-common.py',
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
			'gsettings-desktop-schemas.py',
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

		# exclude package with possible patent/copyright issues
		# when doing release builds
		if not self.cmd_options.release_build:
			self.packages.extend ([
				# BCE streamrecorder
				'lame.py',
			])

		# WebKit-gtk
		# Don't attempt to build webkit-gtk on OS X as it is impossible
		# see: http://www.google-melange.com/gsoc/proposal/review/org/google/gsoc2015/knocte/5668600916475904#c5741031244955648
		if not isinstance (self, DarwinProfile):
			self.packages.extend ([
				'gperf.py',
				'enchant.py',
				'libicu.py',
				'harfbuzz.py',
				'libwebp.py',
				# webkit-gtk3 currently not working
				# 'webkit-gtk3.py'
			])

		# Theme
		self.packages.extend ([
			'librsvg.py',
			'icon-naming-utils.py',
			'hicolor-icon-theme.py',
			'tango-icon-theme.py',
			'adwaita-icon-theme.py'
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
			'orc.py',
			'yasm.py',
			'soundtouch.py',
			'gstreamer.py',
			'gst-plugins-base.py',
			'gst-plugins-good.py',
			'gst-libav'
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
			'mono-addins-gtk3.py',
			'dbus-sharp.py',
			'dbus-sharp-glib.py',
			'taglib-sharp.py',
			'gstreamer-sharp.py',

			# mono-upnp only carries gtk#2 UI bits and they cannot be disabled
			# 'mono-upnp.py',
		])

		# banshee-community-extensions
		self.packages.extend ([
			# lastfm fingerprint
			'fftw.py',
			'libsamplerate.py',
			# openvp
			'libgdiplus.py',
			'libopentk.py',
			'libsdl.py',
			# libglade-gtk3 currently not working
			#'libglade-gtk3.py',

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
