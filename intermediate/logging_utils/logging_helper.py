import logging

# lets create a logger with the name of this file
logging_helper_logger = logging.getLogger(__name__)

# NOTE: if you do not want this specific logger to be triggered when imported in other files, you can set propagate to False 
# logger.propagate = False

logging_helper_logger.info(f"INFO logger from {__name__}")
