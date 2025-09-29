@echo off
echo Starting Book Scraper API server...

REM Activate the API virtual environment
call venv-api\Scripts\activate.bat

REM Start the API server
uvicorn main:app --host 0.0.0.0 --port 8000

pause
