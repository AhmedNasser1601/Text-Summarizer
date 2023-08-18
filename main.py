import json
from .summarizer import Summarizer

def main(input_json):
    # Parse the input JSON to get the Arabic text
    text = json.loads(input_json)["text"]

    # Re-implement the forward pass logic
    model = Summarizer()
    summary = model.forward(text)

    # Return the resulting summary as a JSON object
    return json.dumps({"summary": summary}), 200, {'Content-Type': 'application/json'}
