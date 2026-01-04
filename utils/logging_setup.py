import logging 

def setup_logging():
    #Formatter
    formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(funcName)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)   
    
    #Logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Console Log
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # File Log
    file_handler = logging.FileHandler("autosort.log", encoding="utf-8")
    file_handler.setFormatter(formatter)

    #Aggiunta dei Handler al logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    logging.info("Logging has been configured successfully!")