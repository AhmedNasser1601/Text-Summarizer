import torch
import transformers

class Summarizer:
    def __init__(self):
        self.model_name = "bert-base-multilingual-uncased"
        self.tokenizer = transformers.AutoTokenizer.from_pretrained(self.model_name)
        self.model = transformers.AutoModelForSeq2SeqLM.from_pretrained(self.model_name)

    def forward(self, text):
        inputs = self.tokenizer.encode_plus(
            text,
            max_length=512,
            truncation=True,
            padding="longest",
            return_tensors="pt"
        )
        input_ids = inputs["input_ids"]
        attention_mask = inputs["attention_mask"]

        with torch.no_grad():
            outputs = self.model.generate(
                input_ids=input_ids,
                attention_mask=attention_mask,
                max_length=128,
                num_beams=4,
                early_stopping=True
            )

        summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return summary

