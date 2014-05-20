import os
import shutil
from plistlib import Plist
from util.util import *
from darwinprofile import DarwinProfile

class DarwinLionProfile (DarwinProfile):
	def __init__ (self, prefix = False, m64 = False):
		DarwinProfile.__init__ (self, prefix, m64)

		if self.os_x_minor != 7:
        		raise Exception("You must build this package using the OS X Lion (10.7) SDK (SDK version found: 10.%d)" % (self.os_x_minor))
        	os.environ ['MACOSX_DEPLOYMENT_TARGET'] = '10.7'