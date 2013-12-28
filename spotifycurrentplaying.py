import sys
import win32gui
import xchat
from random import randint

# 	Copyright (c) 2013, FaceHunter
# 	All rights reserved.
# 	Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

# 	1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
# 	2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
# 	3. Neither the name of the contributors may be used to endorse or promote products derived from this software without specific prior written permission.

# 	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
# 	IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

__module_name__ = "SpotifyCurrentPlaying"
__module_version__ = "2.0"
__module_description__ = "Sends the current playing song info to the current channel"

class Spotify(object):
	#	(https://code.google.com/p/pytify/)
	# 	Copyright (c) 2009, Bjørge Næss
	# 	All rights reserved.
	#
	# 	Redistribution and use in source and binary forms, with or without modification,
	# 	are permitted provided that the following conditions are met:
	#
	# 	1. Redistributions of source code must retain the above copyright notice,
	#    	this list of conditions and the following disclaimer.
	# 	2. Redistributions in binary form must reproduce the above copyright notice,
	#    	this list of conditions and the following disclaimer in the
	#    	documentation and/or other materials provided with the distribution.
	# 	3. Neither the name of the Bjørge Næss nor the names of its contributors may
	#    	be used to endorse or promote products derived from this software without
	#    	specific prior written permission.
	#
	# 	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
	# 	ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
	# 	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
	# 	DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
	# 	ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
	# 	(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
	# 	LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
	# 	ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
	# 	(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
	# 	SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
	
	
    _hwnd            = None
	

    def __init__(self):
        try:
            self._hwnd = win32gui.FindWindow("SpotifyMainWindow", None)
        except:
            raise self.SpotifyWindowNotFoundException()

    def getCurrentTrack(self):
        return self._parseWindowTitle()['track']

    def getCurrentArtist(self):
        return self._parseWindowTitle()['artist']

    def _parseWindowTitle(self):
        trackinfo = win32gui.GetWindowText(self._hwnd).split(" - ")

        if len(trackinfo) == 1:
            return {'artist': None, 'track': None}

        artist, track = trackinfo[1].split(" \x96 ")
        return {'artist': artist, 'track': track}

    class SpotifyWindowNotFoundException:
        def __str__(self):
            return "Spotify window not found. Is Spotify really running?"

default_template = "is playing %(randcolor)s%(track)s%(normal)s by %(randcolor2)s%(artist)s%(normal)s in 03Spotify"
template = None

def GetTemplate():
	if not template:
		return default_template
	else:
		return template
		
def SetTemplate(word, word_eol, userdata):
	global template
	template = word_eol[1]
	print "Template updated"
	return xchat.EAT_NONE
	
def PrintTemplate(word, word_eol, userdata):
	print GetTemplate()
	return xchat.EAT_NONE
		
def DoeCurInfo(word, word_eol, userdata):
	try:
		spotify = Spotify()
		
	except:
		xchat.prnt("Spotify is not running")
		return xchat.EAT_NONE
	
	
	xchat.command("ME "+GetTemplate() % {"track":spotify.getCurrentTrack(), "artist":spotify.getCurrentArtist(), "randcolor":""+str(randint(0,15)), "randcolor2":""+str(randint(0,15)), "randcolor3":""+str(randint(0,15)), "normal":""})
	return xchat.EAT_NONE

xchat.hook_command("SPOTIFY", DoeCurInfo, help="Displays current song info")
xchat.hook_command("SETSPOTTEMPL", SetTemplate, help="Set the template for /spotify")
xchat.hook_command("GETSPOTTEMPL", PrintTemplate, help="Get the template for /spotify")
print "pytify loaded"
