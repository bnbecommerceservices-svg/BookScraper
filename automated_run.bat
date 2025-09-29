@echo off
echo Starting automated Book Scraper execution...

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

REM Activate the API virtual environment (has all dependencies needed)
call venv-api\Scripts\activate.bat

REM Run the Python automation script
python automated_run.py

REM Deactivate virtual environment
deactivate

echo Automated execution completed!
echo Check execution_log.txt for details.

pause
