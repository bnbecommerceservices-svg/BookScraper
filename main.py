# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all 3 repos
COPY BookScraper-Automation /app/BookScraper-Automation
COPY BookScraper-Automation-Betterworld /app/BookScraper-Automation-Betterworld
COPY BookScraper-Automation-eBay /app/BookScraper-Automation-eBay

# Install dependencies if requirements.txt exists
RUN pip install --no-cache-dir -r BookScraper-Automation/requirements.txt || true
RUN pip install --no-cache-dir -r BookScraper-Automation-Betterworld/requirements.txt || true
RUN pip install --no-cache-dir -r BookScraper-Automation-eBay/requirements.txt || true

# Default command -> run the first project
CMD ["python3", "BookScraper-Automation/main.py"]
