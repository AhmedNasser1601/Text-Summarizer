import json
from summarizer import summarize, Summarizer

def main(input_json):
    # Parse the input JSON to get the Arabic text
    text = json.loads(input_json)["text"]

    # Create an instance of the Summarizer model
    model = Summarizer()

    # Call the model's forward method with the input text to get the summary
    summary = model.forward(text)

    # Return the resulting summary as a JSON object
    return json.dumps({"summary": summary})