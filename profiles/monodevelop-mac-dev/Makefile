MD_BUILD_EXE="../../../monodevelop/main/build/bin/MonoDevelop.exe"
MD_APP_EXE="../../../md-addins/Xamarin Studio.app/Contents/MacOS/lib/monodevelop/bin/XamarinStudio.exe"
MONO_OPTIONS=--gc=sgen --debug
MD_OPTIONS=--no-redirect
DYLD="../../../md-addins/MonoDevelop.IPhone/build:$DYLD_LIBRARY_PATH"

all:
	./monodevelop-mac-dev.py -b

verbose:
	./monodevelop-mac-dev.py -bv

run:
	DYLD_LIBRARY_PATH=$(DYLD) mono $(MONO_OPTIONS) $(MD_BUILD_EXE) $(MD_OPTIONS)

run-app:
	mono $(MONO_OPTIONS) $(MD_APP_EXE) $(MD_OPTIONS)

aot:
	source md-dev-env && \
		mono --aot $(MONO_INSTALL_PREFIX)/lib/mono/2.0/mscorlib.dll && \
		mono --aot $(MONO_INSTALL_PREFIX)/lib/mono/4.5/mscorlib.dll && \
		for i in $(MONO_INSTALL_PREFIX)/lib/mono/gac/*/*/*.dll; do mono --aot $$i; done

deaot:
	find $(MONO_INSTALL_PREFIX)/lib/mono/2.0 -name *.dylib | xargs rm && \
	find $(MONO_INSTALL_PREFIX)/lib/mono/4.5 -name *.dylib | xargs rm && \
	find $(MONO_INSTALL_PREFIX)/lib/mono/gac -name *.dylib | xargs rm
