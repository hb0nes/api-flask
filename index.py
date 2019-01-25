#!/usr/bin/env python3.7

from flask import Flask
app = Flask(__name__)

@app.route('/')
def usage():
    functions = []
    functions.append(('/', 'View this message again.'))
    functions.append(('/getHostname/[serial]', 'Supply a chassis serial, and retrieve a hostname from Topdesk.'))

    retStr = "This is a RESTful API, created to support Maritime IT.\n\n"
    retStr += '{:25}{}\n'.format('Path','Description')
    retStr += '-'*100+'\n'
    for (k,v) in functions:
        retStr += '{:25}{}\n'.format(k,v)
    return retStr 

@app.route('/getHostname/<serial>')
def usage():