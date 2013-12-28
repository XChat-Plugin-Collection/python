import os, sys
import urllib, urllib2
import xchat

# 	Copyright (c) 2013, FaceHunter
# 	All rights reserved.
# 	Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

# 	1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
# 	2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
# 	3. Neither the name of the contributors may be used to endorse or promote products derived from this software without specific prior written permission.

# 	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
# 	IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

__module_name__ = "PluginDownloader"
__module_version__ = "1.0"
__module_description__ = "Downloads a plugin from the XChat-Plugin-Collection"

URL = "https://github.com/XChat-Plugin-Collection/python"
GET_URL = "https://raw.github.com/XChat-Plugin-Collection/python/master/%(plugin)s.py"

if sys.platform == "win32":
	ADDONS_DIR = xchat.get_info("xchatdir") + "\\addons\\"
else:
	ADDONS_DIR = xchat.get_info("xchatdir")+"/addons/"

def percentage(part, whole):
  return 100 * float(part)/float(whole)
	
def DownloadPlugins(Plugins):
	for plugin in Plugins:
		try:
			urllib2.urlopen(URL+plugin)
		except urllib2.HTTPError:
			print "plugin "+plugin+" does not exist!"
			continue

		urllib.urlretrieve(GET_URL % {"plugin":plugin}, ADDONS_DIR+plugin+".py")
		print plugin+" installed, you can now load it using /py load "+plugin+".py"
		#xchat.command("py load "+plugin+".py")
		
def RemovePlugins(Plugins):
	for plugin in Plugins:
		os.remove(ADDONS_DIR+plugin+".py")
		
def PLUD(word, word_eol, userdata):
	if len(word)==1:
		print "Plugin Downloader version %s" % __module_version__
		return xchat.EAT_ALL
		
	if word[1] == "install":
		if len(word) is not 2:
			print "Usage: /PLUD install <plugins>"
			return xchat.EAT_ALL
			
		plugins = word_eol[2].split(" ")
		DownloadPlugins(plugins)
		return xchat.EAT_ALL
		
	elif word[1] == "remove":
		if len(word) is not 2:
			print "Usage: /PLUD remove <plugins>"
			return xchat.EAT_ALL
			
		plugins = word_eol[2].split(" ")
		RemovePlugins(plugins)
		return xchat.EAT_ALL
	
	elif word[1] == "list":
		xchat.command("py list")
		return xchat.EAT_ALL
	
	else:
		print "Unrecognised command!"
		return xchat.EAT_ALL

xchat.hook_command("PLUD", PLUD, help="/PLUD install <plugin> | Installs a plugin\n/PLUD remove <plugin> | Removes a plugin\n/PLUD list | Lists all plugins")
print __module_name__+" loaded!"
