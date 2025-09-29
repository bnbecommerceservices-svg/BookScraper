@echo off
echo Starting Book Scraper automation...

REM Check if eans.txt files exist
if not exist "BookScraper-Automation\eans.txt" (
    echo Error: BookScraper-Automation\eans.txt not found!
    pause
    exit /b 1
)

if not exist "BookScraper-Automation-Betterworld\eans.txt" (
    echo Error: BookScraper-Automation-Betterworld\eans.txt not found!
    pause
    exit /b 1
)

if not exist "BookScraper-Automation-eBay\eans.txt" (
    echo Error: BookScraper-Automation-eBay\eans.txt not found!
    pause
    exit /b 1
)

REM Run World of Books Scraper
echo Running World of Books Scraper...
call venv-worldofbooks\Scripts\activate.bat
cd BookScraper-Automation
python main.py
cd ..
deactivate

REM Check if World of Books scraper completed successfully
if %ERRORLEVEL% neq 0 (
    echo Error occurred while running World of Books Scraper!
    echo Attempting to continue with other scrapers...
)

REM Run Better World Books Scraper
echo Running Better World Books Scraper...
call venv-betterworld\Scripts\activate.bat
cd BookScraper-Automation-Betterworld
python main.py
cd ..
deactivate

REM Check if Better World Books scraper completed successfully
if %ERRORLEVEL% neq 0 (
    echo Error occurred while running Better World Books Scraper!
    echo Attempting to continue with other scrapers...
)

REM Run eBay Scraper
echo Running eBay Scraper...
call venv-ebay\Scripts\activate.bat
cd BookScraper-Automation-eBay
python main.py
cd ..
deactivate

REM Check if eBay scraper completed successfully
if %ERRORLEVEL% neq 0 (
    echo Error occurred while running eBay Scraper!
    echo Attempting to continue...
)

echo All scrapers have finished running!
echo Check the respective directories for CSV output files.

pause
