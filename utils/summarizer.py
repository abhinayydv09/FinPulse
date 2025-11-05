from transformers import pipeline
from utils.config import SUMMARY_PARAMS

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    summary = summarizer(
            text,
            max_length=SUMMARY_PARAMS["max_length"],
            min_length=SUMMARY_PARAMS["min_length"],
            length_penalty=SUMMARY_PARAMS["length_penalty"],
            num_beams=SUMMARY_PARAMS["num_beams"]
            )
    return summary[0]['summary_text']
