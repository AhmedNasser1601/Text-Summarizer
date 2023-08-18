import json
from nlp_model import ArabicSummarizer

def main(input_json):
    text = json.loads(input_json)["text"]
    summarizer = ArabicSummarizer()
    summary = summarizer.summarize(text)
    return json.dumps({"summary": summary}), 200, {'Content-Type': 'application/json'}