import json

def main(input_json):
    text = json.loads(input_json)["text"]
    summarizer = Summarizer()
    summary = summarizer.forward(text)
    return json.dumps({"summary": summary}), 200, {'Content-Type': 'application/json'}