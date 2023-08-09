from flask import Flask, request, jsonify
import json
import subprocess

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute():
    # Extract the text from the request
    data = request.get_json()
    text = data['text']

    # Execute the summarization script with the text as input
    result = subprocess.run(['python', 'summarizer.py', text], stdout=subprocess.PIPE)

    # Return the result as an HTTP response
    return jsonify(summary=result.stdout.decode('utf-8'))

if __name__ == '__main__':
    app.run(port=5000)