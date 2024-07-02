from flask import Flask, request, render_template
import os
from functions import storeData

import requests  # Import requests to send HTTP requests

OTHER_SERVER_URL = 'http://localhost:5001/message'  # URL of the other server

app = Flask(__name__)

name = 'Tevin'

@app.route('/')
def index():
    # If you post get the page then show the form
    if request.method == 'GET':
        return render_template('index.html')
    
    else:
        global name

        # Get the data from the form
        data = request.form.get('data')

        # grabe current os date and time
        date = os.getenv('%Y-%m-%d')
        time = os.getenv('%H:%M:%S')

        # Store the data in the database
        storeData(name, date, time, data)

        # After storing the data, then send it over to the other server
        requests.post(OTHER_SERVER_URL, json={'name': name, 'date': date, 'time': time, 'data': data})

@app.route('/message', methods=['POST'])
def message():
    # Get the data from the request
    data = request.json

    # Store the data in the database
    storeData(data['name'], data['date'], data['time'], data['data'])


