import json

def summarize_arabic_text(input_text):
    # Implement the logic to summarize the Arabic text using natural language processing techniques
    summarized_sentence = "This is a summarized sentence."
    return summarized_sentence

def main(input_json):
    text = json.loads(input_json)["text"]
    summary = summarize_arabic_text(text)
    return json.dumps({"summary": summary}), 200, {'Content-Type': 'application/json'}