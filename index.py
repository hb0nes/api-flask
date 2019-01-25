#!/usr/bin/env python3.7
from flask import Flask
import pyodbc

server = 'tcp:topdesk'
database = 'topdesk' 
username = 'topdeskuser' 
password = 'topdeskpassword' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

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

@app.route('/getHostname/<serial>', methods=['GET'])
def getHostname(serial):
    cursor.execute("SELECT hostname FROM hardware WHERE serial=?",serial) 
    row = cursor.fetchone() 
    #while row: 
        #print row[0] 
        #row = cursor.fetchone()
    return row[0]