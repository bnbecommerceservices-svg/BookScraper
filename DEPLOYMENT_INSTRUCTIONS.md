# Book Scraper API Deployment Instructions

## Server Requirements
- Docker Engine 20.10+
- Docker Compose 1.29+
- At least 4GB RAM
- At least 20GB free disk space

## Deployment Steps

1. Clone the repository:
```bash
git clone https://github.com/bnbecommerceservices-svg/BookScraper.git
cd BookScraper
```

2. Prepare the EAN files:
- Copy your eans.txt file to each scraper directory:
  - BookScraper-Automation/eans.txt
  - BookScraper-Automation-Betterworld/eans.txt
  - BookScraper-Automation-eBay/eans.txt

3. Update proxy configuration (if needed):
- Update proxy files in each scraper directory if needed:
  - BookScraper-Automation/proxy_worldofbooks.txt
  - BookScraper-Automation-Betterworld/proxy files (if any)
  - BookScraper-Automation-eBay/proxy files (if any)

4. Build and start the containers:
```bash
docker-compose up -d
```

5. Check the logs:
```bash
docker-compose logs -f
```

## API Endpoints

- GET / - Health check endpoint
- GET /run-scraper - Run the default scraper
- GET /run-worldofbooks - Run World of Books scraper
- GET /run-betterworld - Run Better World Books scraper
- GET /run-ebay - Run eBay scraper

## Testing with Postman

1. Send a GET request to http://your-server-ip:8000/ to verify the API is running
2. Send a GET request to any of the scraper endpoints to start scraping:
   - http://your-server-ip:8000/run-worldofbooks
   - http://your-server-ip:8000/run-betterworld
   - http://your-server-ip:8000/run-ebay

## Monitoring

- Check container status: `docker-compose ps`
- View logs: `docker-compose logs -f`
- Stop containers: `docker-compose down`

## Updating the Application

1. Pull the latest code:
```bash
git pull origin main
```

2. Rebuild and restart containers:
```bash
docker-compose down
docker-compose build
docker-compose up -d
```
