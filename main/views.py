# -*- coding: utf-8 -*-

from . import app

@app.route('/')
def top_page():
    return 'Hello, World!'
