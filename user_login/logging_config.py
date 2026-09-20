import logging
from pathlib import Path

logfile = Path("data/logdata.log")

# setting up log
def setup_log():
    logging.basicConfig(level=logging.INFO, 
                        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                        handlers=[logging.FileHandler(logfile, encoding='utf-8')])