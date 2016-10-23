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
from nocdashboard import app
from werkzeug import Response

@app.route('/')
def home_index():
    """ Display a nice Home Page for the user explaining what the hell
    they're doing here. """
    # TODO return render_template call

@app.route("/passthrough", methods=['GET'])
def passthrough_rest_object(source_url):
    """ Passes through a non-CORS locked down JSON object from the origin
    request. """
    if request.method == 'GET':
        reqUrl = request.args.get('url','')
        req = requests.get(reqUrl)
        if req.status_code == 200:
            return req.content
        else:
            return false

@app.route('/passthrough_xml', methods=['GET'])
def passthrough_xml_object():
    """ Passes through a non-CORS locked down XML object from the origin
    request. """
    if request.method == 'GET':
        reqUrl = request.args.get('url','')
        req = requests.get(reqUrl)

        if req.status_code == 200:
            resp = Response(req.content, content_type='text/xml; charset=utf-8')
            resp.headers['Access-Control-Allow-Origin'] = '*'
            #return Response(req.content, content_type='text/xml; charset=utf-8,', headers="Access-Control-Allow-Origin: *")
            return resp
        else:
            return false

@app.route('/passthrough_xml_to_json', methods=['GET'])
def passthrough_xml_to_json():
    """ Retrieves a XML file and then attempts to convert to JSON, and returns
    through the request. """
