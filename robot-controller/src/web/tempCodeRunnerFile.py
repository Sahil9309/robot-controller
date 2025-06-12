from flask import Flask, render_template, jsonify
import os

COORD_FILE = os.path.join(os.path.dirname(__file__), "..", "coordinates.txt")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coordinates')