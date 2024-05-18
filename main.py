from flask import Flask, request, jsonify, render_template
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load summarization pipeline
try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
except Exception as e:
    print(f"Error loading model: {e}")
    summarizer = None

def generate_summary(text, min_length, max_length):
    if summarizer:
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']
    else:
        return "Summarizer model not loaded."

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text')
    min_length = data.get('min_length', 30)
    max_length = data.get('max_length', 130)
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    if max_length <= min_length:
        return jsonify({'error': 'max_length must be greater than min_length'}), 400
    summary = generate_summary(text, min_length, max_length)
    return jsonify({'summary': summary})

@app.route('/')
def serve_index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)