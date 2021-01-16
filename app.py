# -*- coding: utf-8 -*-

import requests
from flask import Flask

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


@app.route('/niji-gazo/')
def tor():
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
    }
    proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
    res = requests.get('http://niji-gazo.com',
                       headers=headers, proxies=proxies)
    return res.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
