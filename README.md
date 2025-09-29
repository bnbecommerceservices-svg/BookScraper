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
