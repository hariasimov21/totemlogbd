#!/usr/bin/env python
import json
from io import StringIO
import flask
import flask_cors
import funciones as fn
import os
import sys
from flask import Response
import threading

#logging.basicConfig(filename='log.log', format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

app = flask.Flask(__name__)
flask_cors.CORS(app, resources=r'/api/*')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def index():
    return "Server is up!\nlogs will be stored in BD"

@app.route('/api/logger', methods=['GET', 'POST'])
def logger():    
    result = flask.request.json
    buffer = StringIO() 
    json.dump(result, buffer)
    entrada = buffer.getvalue()
    entradaJson = json.loads(entrada)
    print(entradaJson)
    fn.desintegraData(entradaJson)
    return 'OK'

@app.route('/api/restart', methods=['POST'])
def restart_app():
    print("Reiniciando aplicacion...")

    def reinicio():
        os.execv(sys.executable, ['python'] + sys.argv)
        

    hilo = threading.Thread(target=reinicio)
    hilo.start()

    return Response('OK', status=200)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5003)