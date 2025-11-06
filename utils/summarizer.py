from transformers import pipeline
from config import SUMMARY_PARAMS

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    if not text or len(text.strip()) == 0:
        return "No summary available."

    try:
        summary = summarizer(
            text,
            max_length=SUMMARY_PARAMS["max_length"],
            min_length=SUMMARY_PARAMS["min_length"],
            length_penalty=SUMMARY_PARAMS["length_penalty"],
            num_beams=SUMMARY_PARAMS["num_beams"]
            )[0]['summary_text']
        return summary.strip()
    
    except Exception as e:
        print(f"Summarization failed: {e}")
        return text[:200] + "..."
