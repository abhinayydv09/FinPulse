import logging
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from config import SUMMARY_PARAMS, MODEL_NAME


# Logging setup
# -------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s"
)

# Load summarization model and tokenizer
# -------------------------------------------------------
try:
    logging.info(f"Loading summarization model: {MODEL_NAME}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    logging.info("Summarization model loaded successfully ✅")
except Exception as e:
    logging.error(f"Failed to load summarization model: {e}")
    summarizer = None

                        
# Summarize text
# -------------------------------------------------------
def summarize_text(text: str) -> str:
    """
    Summarizes input text using HuggingFace model defined in config.py.
    Uses parameters (max_length, min_length, etc.) from SUMMARY_PARAMS.
    """
    if not text or summarizer is None:
        logging.warning("No text provided or summarizer not available.")
        return text if text else "No content to summarize."

    try:
        # Trim text safely (avoid long articles causing overflow)
        input_text = text.strip()[:25000]

        logging.info("Summarizing text of length {len(input_text)} characters...")

        # Use summary parameters from config
        summary_output = summarizer(
            input_text,
            max_length=SUMMARY_PARAMS.get("max_length", 100),
            min_length=SUMMARY_PARAMS.get("min_length", 30),
            length_penalty=SUMMARY_PARAMS.get("length_penalty", 1.0),
            num_beams=SUMMARY_PARAMS.get("num_beams", 6),
            early_stopping=SUMMARY_PARAMS.get("early_stopping", True)
        )

        summary = summary_output[0]["summary_text"].strip()
        logging.info("Summary generated successfully. ")
        return summary

    except Exception as e:
        logging.error(f"Summarization failed: {e}")
        # Return partial text fallback if model fails
        return text[:100] + "..."
                                                                
