FROM python:3.11-slim

WORKDIR /app

# Copy all scraper directories
COPY BookScraper-Automation /app/BookScraper-Automation
COPY BookScraper-Automation-Betterworld /app/BookScraper-Automation-Betterworld
COPY BookScraper-Automation-eBay /app/BookScraper-Automation-eBay

# Copy main API files
COPY main.py /app/main.py
COPY my_scraper.py /app/my_scraper.py

# Install dependencies for all scrapers
RUN pip install --no-cache-dir -r BookScraper-Automation/requirements.txt && \
    pip install --no-cache-dir -r BookScraper-Automation-Betterworld/requirements.txt && \
    pip install --no-cache-dir -r BookScraper-Automation-eBay/requirements.txt && \
    pip install --no-cache-dir fastapi uvicorn

# Create necessary directories
RUN mkdir -p /app/BookScraper-Automation/logs && \
    mkdir -p /app/BookScraper-Automation-Betterworld/logs && \
    mkdir -p /app/BookScraper-Automation-eBay/logs

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
