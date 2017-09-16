#!/usr/bin/env python
#
# Launch HTTP server using an available port between 8000-8100.
# And also launch ${HOME}/bin/watch.rb script, which should be installed,
# to keep watching the port. If any file in this directory is updated,
# the watch.rb script tells Safari to reload a certain tab with specified name.
#

import commands
import os
import SimpleHTTPServer
import SocketServer
import multiprocessing

portnum = 8000
title = commands.getoutput("grep -o '<title>.*</title>' index.html | sed 's/<title>//' | sed 's|</title>||'")
print "title = ",title
cwd = os.getcwd()
print "cwd = ", cwd

while(True):
    outlsof = int(commands.getoutput("lsof -i:{0:d} -P | wc -l".format(portnum)))
    if outlsof != 0:
        portnum += 1
    else:
        break

# os.system('python -m SimpleHTTPServer {0:d} &'.format(portnum))
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", portnum), Handler)
print "serving at port: ", portnum
# httpd.serve_forever()
#...start the server as a separate process
server_process = multiprocessing.Process(target=httpd.serve_forever)
server_process.daemon = True
server_process.start()

url = "localhost:{0:d}".format(portnum)

osascript="osascript -e 'tell application \"Safari\" to open location \"{0:s}\"'".format(url)
print osascript
os.system(osascript)

watchrb="~/bin/watch.rb {0:s} \"{1:s}\"".format(cwd,url)
print watchrb
os.system(watchrb)

