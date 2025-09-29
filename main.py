# main.py (FastAPI API entrypoint)

from fastapi import FastAPI, BackgroundTasks
from my_scraper import run_scraper
import asyncio
import os
import sys

app = FastAPI()

# Add scraper directories to Python path
sys.path.append("/app/BookScraper-Automation")
sys.path.append("/app/BookScraper-Automation-Betterworld")
sys.path.append("/app/BookScraper-Automation-eBay")

@app.get("/")
async def root():
    return {"message": "Book Scraper API is running"}

@app.get("/run-scraper")
async def run_scraper_endpoint(background_tasks: BackgroundTasks):
    # Schedule scraper to run in background
    background_tasks.add_task(run_scraper)
    return {"status": "Scraper started in background"}

@app.get("/run-worldofbooks")
async def run_worldofbooks_scraper(background_tasks: BackgroundTasks):
    """Run World of Books scraper"""
    # Import and run the World of Books scraper
    scraper_dir = "/app/BookScraper-Automation"
    main_py = os.path.join(scraper_dir, "main.py")
    
    async def run_worldofbooks():
        process = await asyncio.create_subprocess_exec(
            sys.executable, main_py,
            cwd=scraper_dir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        stdout, stderr = await process.communicate()
        print(f"World of Books scraper finished with return code {process.returncode}")
        if stdout:
            print(f"stdout: {stdout.decode()}")
        if stderr:
            print(f"stderr: {stderr.decode()}")
    
    background_tasks.add_task(run_worldofbooks)
    return {"status": "World of Books scraper started in background"}

@app.get("/run-betterworld")
async def run_betterworld_scraper(background_tasks: BackgroundTasks):
    """Run Better World Books scraper"""
    # Import and run the Better World Books scraper
    scraper_dir = "/app/BookScraper-Automation-Betterworld"
    main_py = os.path.join(scraper_dir, "main.py")
    
    async def run_betterworld():
        process = await asyncio.create_subprocess_exec(
            sys.executable, main_py,
            cwd=scraper_dir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        stdout, stderr = await process.communicate()
        print(f"Better World Books scraper finished with return code {process.returncode}")
        if stdout:
            print(f"stdout: {stdout.decode()}")
        if stderr:
            print(f"stderr: {stderr.decode()}")
    
    background_tasks.add_task(run_betterworld)
    return {"status": "Better World Books scraper started in background"}

@app.get("/run-ebay")
async def run_ebay_scraper(background_tasks: BackgroundTasks):
    """Run eBay scraper"""
    # Import and run the eBay scraper
    scraper_dir = "/app/BookScraper-Automation-eBay"
    main_py = os.path.join(scraper_dir, "main.py")
    
    async def run_ebay():
        process = await asyncio.create_subprocess_exec(
            sys.executable, main_py,
            cwd=scraper_dir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        stdout, stderr = await process.communicate()
        print(f"eBay scraper finished with return code {process.returncode}")
        if stdout:
            print(f"stdout: {stdout.decode()}")
        if stderr:
            print(f"stderr: {stderr.decode()}")
    
    background_tasks.add_task(run_ebay)
    return {"status": "eBay scraper started in background"}
