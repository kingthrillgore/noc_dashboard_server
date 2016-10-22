#!/usr/bin/env python
"""
    ______  _______ _______ _     _ ______   _____  _______  ______ ______
    |     \ |_____| |______ |_____| |_____] |     | |_____| |_____/ |     \\
    |_____/ |     | ______| |     | |_____] |_____| |     | |    \_ |_____/

    Proxy Requests Library
    Commonly used to pwn CORS headers on resources that don't know no better

"""
import os
import requests

from flask import request, session, url_for, redirect

@app.route('/')
def home_index():
    """ Display a nice Home Page for the user explaining what the hell
    they're doing here. """
    # TODO return render_template call

@app.route("/passthrough/<source_url>")
def passthrough_rest_object(source_url):
    """ Passes through a non-CORS locked down JSON object from the origin
    request. """
    req = requests.get(source_url)
    if req.status_code == 200:
        return req.content
    else:
        return false

@app.route('/passthrough_xml/<source_url>')
def passthrough_xml_object():
    """ Passes through a non-CORS locked down XML object from the origin
    request. """
    req = requests.get(source_url)
    if req.status_code == 200:
        return req.content
    else:
        return false
