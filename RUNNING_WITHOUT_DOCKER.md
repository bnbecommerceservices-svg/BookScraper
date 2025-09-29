# Running Book Scraper API Without Docker

This guide explains how to run the Book Scraper API directly on your local machine without using Docker.

## Prerequisites

- Python 3.11 installed
- pip (Python package manager)
- Git (to clone the repository)

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/bnbecommerceservices-svg/BookScraper.git
cd BookScraper
```

2. Create virtual environments for each scraper:

World of Books Scraper:
```bash
python -m venv venv-worldofbooks
# On Windows:
venv-worldofbooks\Scripts\activate
# On macOS/Linux:
# source venv-worldofbooks/bin/activate

pip install -r BookScraper-Automation/requirements.txt
deactivate
```

Better World Books Scraper:
```bash
python -m venv venv-betterworld
# On Windows:
venv-betterworld\Scripts\activate
# On macOS/Linux:
# source venv-betterworld/bin/activate

pip install -r BookScraper-Automation-Betterworld/requirements.txt
deactivate
```

eBay Scraper:
```bash
python -m venv venv-ebay
# On Windows:
venv-ebay\Scripts\activate
# On macOS/Linux:
# source venv-ebay/bin/activate

pip install -r BookScraper-Automation-eBay/requirements.txt
deactivate
```

3. Create a unified virtual environment for the API:
```bash
python -m venv venv-api
# On Windows:
venv-api\Scripts\activate
# On macOS/Linux:
# source venv-api/bin/activate

pip install -r BookScraper-Automation/requirements.txt
pip install -r BookScraper-Automation-Betterworld/requirements.txt
pip install -r BookScraper-Automation-eBay/requirements.txt
pip install fastapi uvicorn
```

4. Prepare the EAN files:
- Copy your eans.txt file to each scraper directory:
  - BookScraper-Automation/eans.txt
  - BookScraper-Automation-Betterworld/eans.txt
  - BookScraper-Automation-eBay/eans.txt

## Running the Scrapers

### Run World of Books Scraper
```bash
venv-worldofbooks\Scripts\activate
cd BookScraper-Automation
python main.py
```

### Run Better World Books Scraper
```bash
venv-betterworld\Scripts\activate
cd BookScraper-Automation-Betterworld
python main.py
```

### Run eBay Scraper
```bash
venv-ebay\Scripts\activate
cd BookScraper-Automation-eBay
python main.py
```

## Running the API Server

1. Activate the API virtual environment:
```bash
venv-api\Scripts\activate
```

2. Start the API server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

3. Test the API endpoints:
- http://localhost:8000/ - Health check
- http://localhost:8000/run-worldofbooks - Run World of Books scraper
- http://localhost:8000/run-betterworld - Run Better World Books scraper
- http://localhost:8000/run-ebay - Run eBay scraper

Note that when running the scrapers through the API, they will use the unified virtual environment which has all the dependencies installed.

## Testing with Postman

1. Start the API server as described above
2. Send a GET request to any of the scraper endpoints to start scraping:
   - GET http://localhost:8000/run-worldofbooks
   - GET http://localhost:8000/run-betterworld
   - GET http://localhost:8000/run-ebay

## Benefits of Running Without Docker

1. No need to install Docker Desktop
2. Direct access to the code and files
3. Better debugging capabilities
4. More control over the Python environment

## Considerations

1. You'll need to manage Python environments manually
2. Dependencies need to be installed locally
3. You may need to handle path differences between operating systems
4. The API will use the unified virtual environment for all scrapers
