#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Some explanation about things.'

if __name__ == '__main__':
    app.run()
