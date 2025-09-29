"""
Automated Book Scraper Execution Script
"""
import os
import sys
import subprocess
import logging
import shutil
from datetime import datetime
from pathlib import Path
import error_handling

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('execution_log.txt'),
        logging.StreamHandler(sys.stdout)
    ]
)

def run_scraper(scraper_name, scraper_dir, venv_dir):
    """Run a specific scraper"""
    logging.info(f"Starting {scraper_name}...")
    
    try:
        # Construct the command to run the scraper
        cmd = [
            os.path.join(venv_dir, 'Scripts', 'python.exe'),
            os.path.join(scraper_dir, 'main.py')
        ]
        
        # Run the scraper
        result = subprocess.run(
            cmd,
            cwd=scraper_dir,
            capture_output=True,
            text=True,
            timeout=3600  # 1 hour timeout
        )
        
        # Log the results
        if result.returncode == 0:
            logging.info(f"{scraper_name} completed successfully")
            if result.stdout:
                logging.debug(f"{scraper_name} stdout: {result.stdout}")
        else:
            logging.error(f"{scraper_name} failed with return code {result.returncode}")
            if result.stderr:
                logging.error(f"{scraper_name} stderr: {result.stderr}")
            # Try to recover
            if not error_handling.recover_from_failure(scraper_name, result.stderr):
                raise Exception(f"Recovery failed for {scraper_name}")
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        logging.error(f"{scraper_name} timed out after 1 hour")
        error_handling.recover_from_failure(scraper_name, "Timeout")
        return False
    except Exception as e:
        logging.error(f"Error running {scraper_name}: {str(e)}")
        error_handling.recover_from_failure(scraper_name, str(e))
        return False

def copy_output_files(scraper_name, scraper_dir):
    """Copy output files to consolidated directory"""
    try:
        output_dir = 'output'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Copy CSV files
        csv_files = list(Path(scraper_dir).glob("*.csv"))
        for csv_file in csv_files:
            destination = os.path.join(output_dir, f"{scraper_name}_{csv_file.name}")
            shutil.copy2(csv_file, destination)
            logging.info(f"Copied {csv_file} to {destination}")
        
        # Copy any log files
        log_files = list(Path(scraper_dir).glob("*.log"))
        for log_file in log_files:
            destination = os.path.join(output_dir, f"{scraper_name}_{log_file.name}")
            shutil.copy2(log_file, destination)
            logging.info(f"Copied {log_file} to {destination}")
        
        return True
    except Exception as e:
        logging.error(f"Error copying output files for {scraper_name}: {str(e)}")
        return False

def main():
    """Main execution function"""
    start_time = datetime.now()
    logging.info(f"Starting automated Book Scraper execution at {start_time}")
    
    # Initialize error handling
    if not error_handling.main():
        logging.error("Failed to initialize error handling")
        return False
    
    # Define scrapers
    scrapers = [
        {
            'name': 'WorldOfBooks',
            'dir': 'BookScraper-Automation',
            'venv': 'venv-worldofbooks'
        },
        {
            'name': 'BetterWorldBooks',
            'dir': 'BookScraper-Automation-Betterworld',
            'venv': 'venv-betterworld'
        },
        {
            'name': 'eBay',
            'dir': 'BookScraper-Automation-eBay',
            'venv': 'venv-ebay'
        }
    ]
    
    # Run each scraper
    results = {}
    for scraper in scrapers:
        # Run the scraper
        success = run_scraper(scraper['name'], scraper['dir'], scraper['venv'])
        results[scraper['name']] = success
        
        # Copy output files regardless of success/failure
        copy_output_files(scraper['name'], scraper['dir'])
        
        # Add a small delay between scrapers
        import time
        time.sleep(5)
    
    # Summary
    end_time = datetime.now()
    duration = end_time - start_time
    
    logging.info("=== EXECUTION SUMMARY ===")
    logging.info(f"Start time: {start_time}")
    logging.info(f"End time: {end_time}")
    logging.info(f"Total duration: {duration}")
    
    for scraper_name, success in results.items():
        status = "SUCCESS" if success else "FAILED"
        logging.info(f"{scraper_name}: {status}")
    
    # Validate output files
    error_handling.validate_csv_files('output')
    
    logging.info("Automated execution completed")
    return all(results.values())

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
