# Web application for hunter's ip searching

from flask import Flask, render_template, request, send_from_directory, jsonify, Response, g, flash, redirect
from flask import make_response
import os
import json
import requests

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/result', methods=['POST'])
def result():
    ip_form = request.form['ip_form']
    return render_template('result.html', data=[get_ip_location(ip_form)])
    
@app.route('/get_ip_location')
def get_ip_location(ip):
    with open('../wut.txt') as filename:
        key = filename.read()[:-1]
    print(filename.read)
    return requests.get('https://context.skyhookwireless.com/accelerator/ip?version=2.0&ip={}&prettyPrint=true&key={} &user=eval'.format(ip,key)).content


if __name__ == '__main__':
    app.run(host='ec2-34-202-65-148.compute-1.amazonaws.com', port=8150, debug=True)