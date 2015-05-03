class GstPluginsGoodPackage (GstreamerPackage):
	def __init__ (self):
		GstreamerXzPackage.__init__ (self, 'gstreamer', 'gst-plugins-good',
			'1.4.5', configure_flags = [
				'--disable-gtk-doc',
				'--disable-gdk_pixbuf',
				'--disable-cairo',
				'--disable-jpeg',
				'--disable-libpng',
				'--disable-deinterlace',
				'--disable-taglib',
				'--disable-annodex'
			]
		)

		# FIXME: these should be passed on the Linux profile
		# when we do away with xvideo/xoverlay and replace
		# with Clutter and Cairo
		if Package.profile.name == 'darwin':
			self.configure_flags.extend ([
				'--disable-cairo',
				'--disable-cairo_gobject',
				'--disable-deinterlace',
				'--disable-x',
				'--disable-xvideo',
				'--disable-xshm'
			])

GstPluginsGoodPackage ()
