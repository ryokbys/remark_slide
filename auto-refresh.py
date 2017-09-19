#!/usr/bin/env python
#
# Launch HTTP server using an available port between 8000-8100.
# And also launch ${HOME}/bin/watch.rb script, which should be installed,
# to keep watching the port. If any file in this directory is updated,
# the watch.rb script tells Safari to reload a certain tab with specified name.
#

import commands
import os
from subprocess import Popen,PIPE
import shlex

portnum = 8000
title = commands.getoutput("grep -o '<title>.*</title>' index.html | sed 's/<title>//' | sed 's|</title>||'")
print "title = ",title
cwd = os.getcwd()
print "cwd = ", cwd
browser = 'Safari'
#browser = 'Google Chrome'
print "browser = ", browser

while(True):
    outlsof = int(commands.getoutput("lsof -i:{0:d} -P | wc -l".format(portnum)))
    if outlsof != 0:
        portnum += 1
    else:
        break

cmd = 'http-server -p {0:d}'.format(portnum)
process = Popen(shlex.split(cmd),stdout=PIPE,stderr=PIPE)
print "serving at port: ", portnum

url = "http://localhost:{0:d}".format(portnum)

osascript="osascript -e 'tell application \"{0:s}\" to open location \"{1:s}\"'".format(browser,url)
print osascript
os.system(osascript)

watchrb="~/bin/watch.rb {0:s} \"{1:s}\" {2:s}".format(cwd,url,browser)
print watchrb
os.system(watchrb)

