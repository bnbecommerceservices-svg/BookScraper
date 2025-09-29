import asyncio
import logging
import sys
import os
from datetime import datetime

async def run_scraper():
    """Runs BookScraper-Automation/main.py inside container with real-time logging"""
    scraper_dir = os.path.join(os.path.dirname(__file__), "BookScraper-Automation")
    main_py = os.path.join(scraper_dir, "main.py")

    # Create logs directory if not exists
    logs_dir = os.path.join(scraper_dir, "logs")
    os.makedirs(logs_dir, exist_ok=True)

    # Log filename with timestamp
    log_file = os.path.join(logs_dir, f"scraper_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    logging.info(f"Starting scraper. Realtime log will also be written to {log_file}")

    process = await asyncio.create_subprocess_exec(
        sys.executable, main_py,
        cwd=scraper_dir,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    # Open log file for appending real-time logs
    with open(log_file, "w", encoding="utf-8") as f:

        async def log_stream(stream, level, prefix):
            while True:
                line = await stream.readline()
                if not line:
                    break
                decoded = line.decode().rstrip()
                # Log to console
                logging.log(level, f"{prefix} {decoded}")
                # Log to file
                f.write(f"{prefix} {decoded}\n")
                f.flush()

        # Run both stdout + stderr logging concurrently
        await asyncio.gather(
            log_stream(process.stdout, logging.INFO, "[stdout]"),
            log_stream(process.stderr, logging.ERROR, "[stderr]")
        )

    # Wait for process to finish
    await process.wait()
    logging.info("Finished running BookScraper-Automation/main.py")
