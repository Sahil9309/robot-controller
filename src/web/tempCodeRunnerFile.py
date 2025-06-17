from flask import Flask, render_template, jsonify
import os

COORD_FILE = os.path.join(os.path.dirname(__file__), "..", "coordinates.txt")

app = Flask(__name__)

@app.route('/coordinates')
def coordinates():
    try:
        with open(COORD_FILE, "r") as f:
            x_str, y_str = f.read().strip().split(",")
            x, y = int(x_str), int(y_str)
    except Exception:
        x, y = 0, 0
    return jsonify({"x": x, "y": y})
