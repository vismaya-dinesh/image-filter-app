from flask import Flask, request, send_file
from flask_cors import CORS
import cv2
import numpy as np
import io

app = Flask(__name__)
CORS(app)

def apply_filter(img, filter_type):
    if filter_type == 'grayscale':
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'blur':
        return cv2.GaussianBlur(img, (15, 15), 0)
    elif filter_type == 'edge':
        return cv2.Canny(img, 100, 200)
    return img

@app.route('/filter', methods=['POST'])
def filter_image():
    file = request.files['image']
    filter_type = request.form['filter']

    in_memory_file = file.read()
    npimg = np.frombuffer(in_memory_file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    filtered = apply_filter(img, filter_type)

    if len(filtered.shape) == 2:
        filtered = cv2.cvtColor(filtered, cv2.COLOR_GRAY2BGR)
    
    _, buffer = cv2.imencode('.jpg', filtered)
    io_buf = io.BytesIO(buffer)

    return send_file(io_buf, mimetype='image/jpeg')


if __name__ == "__main__":
    app.run(debug=True)