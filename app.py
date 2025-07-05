from flask import Flask, request, render_template
import os
from utils.color_utils import is_grayscale, extract_dominant_colors
from utils.ocr_utils import extract_text
from utils.object_detection import detect_objects
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No image uploaded!', 400
    file = request.files['image']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    # Run analysis
    grayscale = is_grayscale(filepath)
    text = extract_text(filepath)
    objects = detect_objects(filepath)
    colors = extract_dominant_colors(filepath, num_colors=5)
    return render_template('result.html',
                           image_path=filepath,
                           grayscale=grayscale,
                           text=text,
                           objects=objects,
                           colors=colors)
if __name__ == '__main__':
    app.run(debug=True)
