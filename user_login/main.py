import logging

from helpers import *
from logging_config import setup_log

logger = logging.getLogger(__name__)
ApplicationRun = False

def initialize():
    LoadData = JSON_Storage.load_data()
    importData = User_Manager.importData(LoadData["data"])
    AuthData = User_Manager.authdata()

    if importData["status"] and AuthData["status"] and LoadData["status"]:
        logger.info("Initialize: User manager initialised successfully.")
        return True
    else:
        if not LoadData["status"]:
            logger.error("Initialize: Data loading failed: %s", LoadData["message"])
        if not importData["status"]:
                    logger.error("Initialize: User data import failed: %s", importData["message"])
        if not AuthData["status"]:
                    logger.error("Initialize: Authentication data loading failed: %s", AuthData["message"])
        logger.error("Initialize: Failed to initialise user manager.")
        return False
        
if __name__ == '__main__':
    setup_log()
    if initialize():
        ApplicationRun = True
    else:
        print("Failed to initialize.")
    Main(ApplicationRun)