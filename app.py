# -*- coding: utf-8 -*-

from pathlib import Path
import requests
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def top_page():
    res = requests.get('https://ipinfo.io')
    return res.content


@app.route('/torrc')
def torrc():
    return Response(Path('torrc').read_bytes(), mimetype='text/plain')


@app.route('/test/')
def test():
    url = request.args.get('url', 'https://ipinfo.io')
    headers = {
        'User-Agent': request.headers.get('User-Agent')
    }
    if 'tor' in request.args:
        proxies = {
            'http': 'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050'
        }
    else:
        proxies = {}
    res = requests.get(url, headers=headers, proxies=proxies)
    return res.content


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
