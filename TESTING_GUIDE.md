# Testing Guide for Book Scraper API

This guide provides instructions for testing all aspects of the Book Scraper API.

## Prerequisites

- Python 3.11 installed
- Git installed
- Internet connection
- Sample EAN files for testing

## Testing Docker Deployment

1. Clone the repository:
```bash
git clone https://github.com/bnbecommerceservices-svg/BookScraper.git
cd BookScraper
```

2. Build and start the containers:
```bash
docker-compose up -d
```

3. Verify containers are running:
```bash
docker-compose ps
```

4. Test API endpoints:
- GET http://localhost:8000/ - Should return health check message
- GET http://localhost:8000/run-worldofbooks - Should start World of Books scraper
- GET http://localhost:8000/run-betterworld - Should start Better World Books scraper
- GET http://localhost:8000/run-ebay - Should start eBay scraper

5. Check logs:
```bash
docker-compose logs -f
```

6. Stop containers:
```bash
docker-compose down
```

## Testing Non-Docker Deployment

1. Clone the repository:
```bash
git clone https://github.com/bnbecommerceservices-svg/BookScraper.git
cd BookScraper
```

2. Run setup script:
```cmd
setup.bat
```

3. Prepare test EAN files:
Create eans.txt files in each scraper directory with a few test EANs:
- BookScraper-Automation/eans.txt
- BookScraper-Automation-Betterworld/eans.txt
- BookScraper-Automation-eBay/eans.txt

4. Test individual scrapers:
```cmd
run_scrapers.bat
```

5. Test API server:
```cmd
run_api.bat
```
Then test endpoints with Postman or curl:
- GET http://localhost:8000/
- GET http://localhost:8000/run-worldofbooks
- GET http://localhost:8000/run-betterworld
- GET http://localhost:8000/run-ebay

## Testing Automated Local Execution

1. Follow steps 1-3 from "Testing Non-Docker Deployment"

2. Run automated execution:
```cmd
automated_run.bat
```

3. Verify:
- Check execution_log.txt for execution details
- Check output directory for CSV files
- Verify error handling by temporarily disconnecting internet during scraper run

## Testing Error Handling

1. Test missing EAN files:
- Remove one or more eans.txt files
- Run automated_run.bat
- Verify appropriate error messages

2. Test scraper failures:
- Temporarily modify a scraper to raise an exception
- Run automated execution
- Verify error is logged and execution continues

3. Test recovery:
- Introduce a temporary network issue during scraper execution
- Verify recovery mechanisms work
- Check that subsequent scrapers still run

## Expected Results

### Docker Deployment
- Containers start successfully
- API endpoints respond correctly
- Scrapers execute when endpoints are called
- Output files are created in container filesystem

### Non-Docker Deployment
- Virtual environments are created successfully
- Dependencies are installed without errors
- Scrapers run and produce CSV output
- API server starts and responds to requests

### Automated Local Execution
- All three scrapers run sequentially
- CSV output files are consolidated in output directory
- Execution log contains detailed information
- Errors are handled gracefully and logged
- Execution continues even if one scraper fails

## Troubleshooting

### Common Issues

1. **Docker not running**
   - Ensure Docker Desktop is installed and running
   - Check Docker service status

2. **Permission denied errors**
   - Run command prompt as administrator
   - Check file permissions

3. **Missing dependencies**
   - Re-run setup.bat
   - Check internet connection

4. **Scrapers not producing output**
   - Verify EAN files contain valid EANs
   - Check proxy settings if applicable
   - Review scraper-specific logs

### Log Locations

- Docker: `docker-compose logs`
- Non-Docker: Check scraper-specific log files
- Automated execution: `execution_log.txt` and `error_recovery.log`
