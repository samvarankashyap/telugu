import os
import json
from flask import Flask
from flask import render_template
from flask import Flask, request, send_from_directory
from text_processor import *

app = Flask(__name__,static_url_path='/static')


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('./static/js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('./static/css', path)


@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/gethtml')
def get_html():
    html = call_for_data(True,True)
    return json.dumps(html)

ip = os.getenv("IP", "0.0.0.0")
port = int(os.getenv("PORT", 80))


if __name__ == '__main__':
    app.debug = True
    app.run(host=ip, port=port)
