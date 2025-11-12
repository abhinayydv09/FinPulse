# Base image
FROM python:3.12-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download HuggingFace model during build
RUN python -c "from transformers import AutoTokenizer, AutoModelForSeq2SeqLM; \
AutoTokenizer.from_pretrained('sshleifer/distilbart-cnn-12-6'); \
AutoModelForSeq2SeqLM.from_pretrained('sshleifer/distilbart-cnn-12-6')"

# Copy project files
COPY . .

# Default command
CMD ["python", "main.py"]
