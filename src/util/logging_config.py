import logging, logging.config, os, json

def setup_logging(default_path="config/logging.ini", default_level=logging.INFO):
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    if os.path.exists(default_path):
        logging.config.fileConfig(default_path, disable_existing_loggers=False)
    else:
        logging.basicConfig(level=default_level,
                            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    logging.getLogger(__name__).debug("Logging initialized")