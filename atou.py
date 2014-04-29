#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xchat

# Ascii to Unicode - Made for Seth "Takeru" Lunsford
# Copyright (c) 2014, Avail
# All rights reserved.
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

# 1) You must re-link the original source on GitHub, https://github.com/XChat-Plugin-Collection/python/blob/master/atou.py
# 2) You can modify the __module_author__ line only if you keep the original's author name. E.g: __module_author__ = "Avail, FaceHunter"

### MODULE INFO ###
__module_name__ = "Ascii -> Unicode"
__module_version__ = "1.1"
__module_description__ = "Converts normal text to fullwidth"
__module_author__ = "Avail"

### IRC CODES ###
IRC_BOLD =           "\002"

### SPECIFY WIDEMAP CHAR SET RANGE ###
WIDE_MAP = dict((i, i + 0xFEE0) for i in xrange(0x21, 0x7F))
WIDE_MAP[0x20] = 0x3000
 
### THIS RETURNS THE WIDENED STRING ###
def widen(s):
    return unicode(s).translate(WIDE_MAP)

### XCHAT/HEXCHAT HOOK THAT SENDS THE TEXT/SENDS ###
### OUT AN EXCEPTION IF NO TEXT IS SPECIFIED ###
def atou(word, word_eol, data):
    try:
        xchat.command("say 【"+ widen(word_eol[1].decode('utf-8')).encode('utf-8')+ "】")
    except IndexError:
        xchat.prnt("No text specified. Please write something after /atou")
    
xchat.hook_command("atou", atou, help="/atou - Converts normal text to full-width")
xchat.prnt( IRC_BOLD + __module_name__ + IRC_BOLD +" (v "+ IRC_BOLD + __module_version__ + IRC_BOLD +") by "+ IRC_BOLD + __module_author__ + IRC_BOLD +" loaded." )
