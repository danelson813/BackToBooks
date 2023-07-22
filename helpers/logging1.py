import logging


def logger_module():
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("data/info.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s: %(message)s"))
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s: %(message)s"))
    logger.addHandler(stream_handler)
    return logger
