import json
from summarizer import summarize

def main(input_json):
    # Parse the input JSON to get the Arabic text
    text = json.loads(input_json)["text"]

    # Call the summarizer function
    summary = summarize(text)

    # Return the resulting summary as a JSON object
    return json.dumps({"summary": summary})