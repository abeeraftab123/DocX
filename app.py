from flask import Flask, request, jsonify, render_template
import os
from utils.text_extraction import extract_text
from utils.question_answering import answer_question


app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    text = extract_text(file_path)
    return jsonify({'text': text})

@app.route('/answer', methods=['POST'])
def get_answer():
    data = request.json
    context = data['context']
    question = data['question']
    answer = answer_question(context, question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)