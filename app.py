#!/usr/bin/env python

import os

from flask import Flask
from flask import render_template
from werkzeug import SharedDataMiddleware

app = Flask(__name__)
#TODO(ankitr): set up external config
app.config['DEBUG'] = True
basedir = os.path.dirname(os.path.abspath(__file__))

if app.config['DEBUG']:
    # Use Flask to serve the static files when we're debugging
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
      '/': os.path.join(basedir, 'static')
    })

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
