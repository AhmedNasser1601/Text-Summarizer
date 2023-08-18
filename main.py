import json
from .model import Summarizer

def main(input_json):
    # Parse the input JSON to get the Arabic text
    text = json.loads(input_json)["text"]

    # Create an instance of the Summarizer class
    summarizer = Summarizer()

    # Use the Summarizer instance to generate the summary
    summary = summarizer.forward(text)

    # Return the resulting summary as a JSON object
    return json.dumps({"summary": summary}), 200, {'Content-Type': 'application/json'}
