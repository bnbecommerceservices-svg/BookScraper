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

REM Create a directory for consolidated output if it doesn't exist
if not exist "output" (
    mkdir output
)

REM Record start time
echo Execution started at %date% %time% > execution_log.txt

REM Run World of Books Scraper
echo Running World of Books Scraper...
call venv-worldofbooks\Scripts\activate.bat
cd BookScraper-Automation
python main.py
cd ..
deactivate

REM Check if World of Books scraper completed successfully
if %ERRORLEVEL% neq 0 (
    echo Error occurred while running World of Books Scraper! >> execution_log.txt
    echo Attempting to continue with other scrapers...
) else (
    echo World of Books Scraper completed successfully. >> execution_log.txt
)

REM Copy output files to consolidated directory
echo Copying World of Books output files...
copy "BookScraper-Automation\*.csv" output\ > nul 2>&1

REM Run Better World Books Scraper
echo Running Better World Books Scraper...
call venv-betterworld\Scripts\activate.bat
cd BookScraper-Automation-Betterworld
python main.py
cd ..
deactivate

REM Check if Better World Books scraper completed successfully
if %ERRORLEVEL% neq 0 (
    echo Error occurred while running Better World Books Scraper! >> execution_log.txt
    echo Attempting to continue with other scrapers...
) else (
    echo Better World Books Scraper completed successfully. >> execution_log.txt
)

REM Copy output files to consolidated directory
echo Copying Better World Books output files...
copy "BookScraper-Automation-Betterworld\*.csv" output\ > nul 2>&1

REM Run eBay Scraper
echo Running eBay Scraper...
call venv-ebay\Scripts\activate.bat
cd BookScraper-Automation-eBay
python main.py
cd ..
deactivate

REM Check if eBay scraper completed successfully
if %ERRORLEVEL% neq 0 (
    echo Error occurred while running eBay Scraper! >> execution_log.txt
    echo Attempting to continue...
) else (
    echo eBay Scraper completed successfully. >> execution_log.txt
)

REM Copy output files to consolidated directory
echo Copying eBay output files...
copy "BookScraper-Automation-eBay\*.csv" output\ > nul 2>&1

REM Record end time
echo Execution finished at %date% %time% >> execution_log.txt

echo All scrapers have finished running!
echo Check the 'output' directory for all CSV files.
echo Check execution_log.txt for details.

pause
