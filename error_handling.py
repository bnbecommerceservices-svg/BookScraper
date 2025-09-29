"""
Error Handling and Recovery Module for Book Scraper
"""
import os
import sys
import shutil
import logging
from datetime import datetime
from pathlib import Path

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('error_recovery.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

def check_and_create_directories():
    """Create necessary directories if they don't exist"""
    directories = ['output', 'logs', 'temp']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logging.info(f"Created directory: {directory}")

def check_ean_files():
    """Check if required EAN files exist"""
    required_files = [
        "BookScraper-Automation/eans.txt",
        "BookScraper-Automation-Betterworld/eans.txt",
        "BookScraper-Automation-eBay/eans.txt"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
            logging.error(f"Missing required file: {file_path}")
    
    if missing_files:
        raise FileNotFoundError(f"Missing required EAN files: {', '.join(missing_files)}")
    
    logging.info("All required EAN files found")

def validate_csv_files(directory):
    """Validate CSV files in a directory"""
    try:
        csv_files = list(Path(directory).glob("*.csv"))
        for csv_file in csv_files:
            # Check if file is not empty
            if csv_file.stat().st_size == 0:
                logging.warning(f"Empty CSV file found: {csv_file}")
            else:
                logging.info(f"Validated CSV file: {csv_file}")
        return True
    except Exception as e:
        logging.error(f"Error validating CSV files in {directory}: {str(e)}")
        return False

def backup_previous_runs():
    """Backup previous run outputs"""
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = f"backup_{timestamp}"
        
        if os.path.exists('output') and os.listdir('output'):
            shutil.copytree('output', backup_dir)
            logging.info(f"Backed up previous output to {backup_dir}")
        
        return True
    except Exception as e:
        logging.error(f"Error during backup: {str(e)}")
        return False

def cleanup_temp_files():
    """Clean up temporary files"""
    try:
        if os.path.exists('temp'):
            shutil.rmtree('temp')
            os.makedirs('temp')
            logging.info("Cleaned up temp directory")
        return True
    except Exception as e:
        logging.error(f"Error cleaning temp directory: {str(e)}")
        return False

def recover_from_failure(step, error):
    """Attempt to recover from a scraper failure"""
    logging.error(f"Failure in {step}: {str(error)}")
    
    # Try to clean up and continue
    try:
        cleanup_temp_files()
        logging.info(f"Attempting to continue after failure in {step}")
        return True
    except Exception as e:
        logging.error(f"Recovery failed: {str(e)}")
        return False

def main():
    """Main error handling and recovery function"""
    logging.info("Starting error handling and recovery process")
    
    try:
        check_and_create_directories()
        check_ean_files()
        backup_previous_runs()
        cleanup_temp_files()
        logging.info("Error handling and recovery initialization completed successfully")
        return True
    except Exception as e:
        logging.error(f"Error during initialization: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
