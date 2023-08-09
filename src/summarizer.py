import torch
import torch.nn as nn
import torch.nn.functional as F
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

class Summarizer(nn.Module):
    def __init__(self):
        super(Summarizer, self).__init__()
        # Define the model architecture here
        self.fc = nn.Linear(input_size, output_size)

    def forward(self, text):
        # Implement the forward pass logic here
        # Tokenize the text
        words = word_tokenize(text)

        # Create a frequency table to keep the score of each word
        freq_table = dict()
        for word in words:
            word = word.lower()
            if word in stopwords.words('arabic'):
                continue
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1

        # Calculate the score of each sentence
        sentences = sent_tokenize(text)
        sentence_scores = dict()
        for sentence in sentences:
            for word, freq in freq_table.items():
                if word in sentence.lower():
                    if sentence in sentence_scores:
                        sentence_scores[sentence] += freq
                    else:
                        sentence_scores[sentence] = freq

        # Get the average score for the sentences
        average_score = sum(sentence_scores.values()) / len(sentence_scores)

        # Generate the summary
        summary = ''
        for sentence in sentences:
            if sentence in sentence_scores and sentence_scores[sentence] > (1.2 * average_score):
                summary += " " + sentence

        return summary

from .summarizer import Summarizer

def summarize(text):
    # Create an instance of the Summarizer model
    model = Summarizer()

    # Call the model's forward method with the input text to get the summary
    summary = model.forward(text)

    return summary