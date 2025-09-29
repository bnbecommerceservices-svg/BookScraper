@echo off
echo Setting up Book Scraper environment...

REM Create virtual environments for each scraper
echo Creating virtual environment for World of Books scraper...
python -m venv venv-worldofbooks

echo Creating virtual environment for Better World Books scraper...
python -m venv venv-betterworld

echo Creating virtual environment for eBay scraper...
python -m venv venv-ebay

echo Creating unified virtual environment for API...
python -m venv venv-api

REM Activate World of Books environment and install dependencies
echo Installing dependencies for World of Books scraper...
call venv-worldofbooks\Scripts\activate.bat
pip install -r BookScraper-Automation\requirements.txt
deactivate

REM Activate Better World Books environment and install dependencies
echo Installing dependencies for Better World Books scraper...
call venv-betterworld\Scripts\activate.bat
pip install -r BookScraper-Automation-Betterworld\requirements.txt
deactivate

REM Activate eBay environment and install dependencies
echo Installing dependencies for eBay scraper...
call venv-ebay\Scripts\activate.bat
pip install -r BookScraper-Automation-eBay\requirements.txt
deactivate

REM Activate API environment and install dependencies
echo Installing dependencies for API...
call venv-api\Scripts\activate.bat
pip install -r BookScraper-Automation\requirements.txt
pip install -r BookScraper-Automation-Betterworld\requirements.txt
pip install -r BookScraper-Automation-eBay\requirements.txt
pip install fastapi uvicorn
deactivate

echo Setup complete! All virtual environments created and dependencies installed.
echo To run the scrapers, execute run_scrapers.bat
pause
