from redis import Redis

from flask import Flask, request, jsonify

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import io
import os
import threading
from firebase import firebase

from flask_cors import CORS
import flask

import common
import database

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/api/booking/', methods=['GET', 'POST'])
def booking():
    if flask.request.method == 'POST':
        id = request.form.get('id')
        store = request.form.get('store')
        pid = request.form.get('pid')
        size = request.form.get('size')
        amount = request.form.get('amount')
    else:
        id = request.args.get('id')
        store = request.args.get('store')
        pid = request.args.get('pid')
        size = request.args.get('size')
        amount = request.args.get('amount')

    print(id, store, pid, size, amount)

    response = {}
    response["MESSAGE"] = f"Booking finish 1 time!!"

    # store = 'architectureandsneakers'
    # pid = '151555065'
    # size = '27.0'
    # amount = 1
    print('start booking', id)

    xxx = threading.Thread(target=common.booking, args=(store, pid, size, amount, id))
    xxx.start()
    xxx.join()
    print('end booking', id)

    # Return the response in json format
    return jsonify([response])

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello from Docker! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
