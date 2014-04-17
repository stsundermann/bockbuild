import os
import shutil
from plistlib import Plist
from util.util import *
from darwinprofile import DarwinProfile

class DarwinLionProfile (DarwinProfile):
	def __init__ (self, prefix = False, m64 = False):
		DarwinProfile.__init__ (self, prefix, m64)

		if self.os_x_minor != 7:
        		raise Exception("You must build this package using the OS X 10.%d SDK (SDK version found: %d)" %(self.os_x_minor_required,self.os_x_minor))
