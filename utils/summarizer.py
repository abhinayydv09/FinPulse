from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from config import SUMMARY_PARAMS, MODEL_NAME
import os

# Disable TensorFlow OneDNN optimizations (optional)
os.environ["TF_ENABLE_ONEDNN_OPTS"] = '0'

# HuggingFace cache directory
HF_CACHE_DIR = os.path.expanduser("~/.cache/huggingface")

# Load model and tokenizer
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=HF_CACHE_DIR)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME, cache_dir=HF_CACHE_DIR)
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
except Exception as e:
    print(f"Error loading model: {e}")
    summarizer = None

def summarize_text(text: str) -> str:
    if not text or summarizer is None:
        return text if text else "No content to summarize."
    
    try:
        summary_output = summarizer(
            text,
            max_length=100,
            min_length=30,
            length_penalty=1.0,
            num_beams=6,
            early_stopping=True
        )
        return summary_output[0]['summary_text']
    except Exception as e:
        print(f"Summarization failed: {e}")
        return text[:100] + "..."
