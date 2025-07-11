from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import os

COORD_FILE = "/tmp/coordinates.txt"

app = Flask(__name__, static_folder='static', template_folder='templates')

CORS(app)
socketio = SocketIO(app)

@app.route('/')
def index():
    print("Serving index.html")
    return render_template('index.html')

@app.route('/coordinates')
def coordinates():
    try:
        with open(COORD_FILE, "r") as f:
            x_str, y_str = f.read().strip().split(",")
            x, y = int(x_str), int(y_str)
    except Exception:
        x, y = 0, 0
    return jsonify({"x": x, "y": y})

@app.route('/set_coordinates', methods=['POST'])
def set_coordinates():
    data = request.get_json()
    x = data.get('x', 0)
    y = data.get('y', 0)
    with open(COORD_FILE, "w") as f:
        f.write(f"{x},{y}")
    return jsonify({"status": "ok"})

@socketio.on('offer')
def handle_offer(data):
    emit('offer', data, broadcast=True)

@socketio.on('answer')
def handle_answer(data):
    emit('answer', data, broadcast=True)

@socketio.on('ice-candidate')
def handle_ice(data):
    emit('ice-candidate', data, broadcast=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5050))
    socketio.run(app, host='0.0.0.0', port=port)