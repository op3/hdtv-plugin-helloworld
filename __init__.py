#!/usr/bin/env python

import hdtv.ui
import hdtv.cmdline

def helloworld(args=None):
    hdtv.ui.msg("Hello World!")

hdtv.cmdline.AddCommand("helloworld", helloworld)
helloworld()

hdtv.ui.debug("Loaded helloworld plugin")
