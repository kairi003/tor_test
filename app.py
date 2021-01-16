# -*- coding: utf-8 -*-

from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def top_page():
    proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
    try:
        res = requests.get('https://ipinfo.io', proxies=proxies)
    except:
        res = requests.get('https://ipinfo.io')
    return res.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
