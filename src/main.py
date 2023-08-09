import json
from summarizer import summarize, Summarizer

def main(input_json):
    # Parse the input JSON to get the Arabic text
    text = json.loads(input_json)["text"]

    # Re-implement the forward pass logic
    summary = model.forward(text)

    # Ensure that the `text` variable is properly declared or assigned a value
    text = json.loads(input_json)["text"]

    # Return the resulting summary as a JSON object
    return json.dumps({"summary": summary}), 200, {'Content-Type': 'application/json'}