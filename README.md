# Book Scraper API

This project contains three book scrapers bundled into a single API:
1. World of Books Scraper
2. Better World Books Scraper
3. eBay Scraper

## Project Structure
- BookScraper-Automation - World of Books scraper
- BookScraper-Automation-Betterworld - Better World Books scraper
- BookScraper-Automation-eBay - eBay scraper
- main.py - FastAPI application with endpoints for each scraper
- my_scraper.py - Shared scraper functionality
- Dockerfile - Docker configuration
- docker-compose.yml - Docker Compose configuration

## API Endpoints
- GET / - Health check endpoint
- GET /run-scraper - Run the default scraper
- GET /run-worldofbooks - Run World of Books scraper
- GET /run-betterworld - Run Better World Books scraper
- GET /run-ebay - Run eBay scraper

## Deployment
See DEPLOYMENT_INSTRUCTIONS.md for detailed deployment steps.

## Running with Docker (Recommended for Deployment)

1. Build and start the containers:
```bash
docker-compose up -d
```

2. Test the API endpoints:
- http://localhost:8000/ - Health check
- http://localhost:8000/run-worldofbooks - Run World of Books scraper
- http://localhost:8000/run-betterworld - Run Better World Books scraper
- http://localhost:8000/run-ebay - Run eBay scraper

## Running Without Docker (For Development/Testing)

See RUNNING_WITHOUT_DOCKER.md for detailed instructions on running the application without Docker.

This approach is better for:
- Development and debugging
- Running on systems where Docker is not available
- Direct file access and modification

## Automated Local Execution (Without Docker)

For completely automated execution on your local PC:

1. Execute setup.bat to install all dependencies:
```cmd
setup.bat
```

2. Prepare your EAN files:
- Copy your eans.txt file to each scraper directory:
  - BookScraper-Automation/eans.txt
  - BookScraper-Automation-Betterworld/eans.txt
  - BookScraper-Automation-eBay/eans.txt

3. Execute automated_run.bat to run all scrapers:
```cmd
automated_run.bat
```

This script will:
- Run all three scrapers automatically
- Handle errors and continue execution
- Consolidate all CSV output files into a single 'output' directory
- Log execution details to execution_log.txt

Alternative options:
- Run individual scrapers: run_scrapers.bat
- Run the API server: run_api.bat
