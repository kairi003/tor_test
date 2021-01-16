# -*- coding: utf-8 -*-

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def top_page():
    res = requests.get('https://ipinfo.io')
    return res.text


@app.route('/tor/')
def tor():
    proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
    res = requests.get('https://ipinfo.io', proxies=proxies)
    return res.text


@app.route('/test/')
def test():
    url = request.args.get('url', 'https://ipinfo.io')
    headers = {
        'User-Agent': request.headers.get('User-Agent')
    }
    proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
    res = requests.get(url, headers=headers, proxies=proxies)
    return res.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
