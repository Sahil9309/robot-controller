from flask import Flask, render_template, jsonify, request, send_from_directory
import os
import base64

COORD_FILE = "/tmp/coordinates.txt"
FRAME_FILE = "/tmp/last_frame.jpg"

app = Flask(__name__)

@app.route('/')
def index():
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

@app.route('/upload_frame', methods=['POST'])
def upload_frame():
    data_url = request.data.decode()
    if data_url.startswith('data:image'):
        header, encoded = data_url.split(',', 1)
        with open(FRAME_FILE, "wb") as f:
            f.write(base64.b64decode(encoded))
    return '', 204

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('/tmp', filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)