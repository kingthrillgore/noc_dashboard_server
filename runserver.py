#!/usr/bin/env python
"""
    ______  _______ _______ _     _ ______   _____  _______  ______ ______
    |     \ |_____| |______ |_____| |_____] |     | |_____| |_____/ |     \\
    |_____/ |     | ______| |     | |_____] |_____| |     | |    \_ |_____/

    NOC Dashboard Server
    version whatever

"""
import os
import sys
from nocdashboard import app, ProxyRequests

def usage():
    """ Display how to use the Server. """
    print """
    If you are seeing this message, Congratulations! You ignored the README.md
    and felt like you knew what you were doing. Good job at that.

    In all seriousness, most of what you need to know is in the README.md, so
    check it out to get an idea on what is available to you here and how to use
    it with the NOC Dashboard application.

    Remember to set the path in the NOC Dashboard in the config.js, and to enable
    the needed settings as required. The README.md and the docs folder contain
    all that you need to know.

    The Default Port is 4510, which can be changed by modifying the Config file.
    If you need to run this within a larger app structure, there are examples of
    gunicorn and Nginx WSGI configs in the server_configs directory. If all else
    fails you can always proxy pass the requests through Apache or Nginx. You
    can find information about this on Google or Stack Overflow.

    Have fun.
    """ #% (sys.argv[0])

def main():
    """ Main hook that runs when the server itself is started. """
    print "NOC Dashboard Server version 0.0.0-indev (Oh baby a triple!)"

    # Gets Config file

    # Tell the user the location of the Server
    app.run()

if __name__ == '__main__':
    main()
