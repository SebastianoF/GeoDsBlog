import logging
from logging import LogRecord


class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    green = "\033[92m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    my_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    dict_formats = {
        logging.DEBUG: grey + my_format + reset,
        logging.INFO: green + my_format + reset,
        logging.WARNING: yellow + my_format + reset,
        logging.ERROR: red + my_format + reset,
        logging.CRITICAL: bold_red + my_format + reset,
    }

    def format(self, record: LogRecord) -> str:
        log_format = self.dict_formats.get(record.levelno)
        formatter = logging.Formatter(log_format)
        return formatter.format(record)


def get_logger(filename: str) -> logging.Logger:
    """logging factory"""
    filename = filename.split(".")[-1]
    if filename in logging.root.manager.loggerDict:  # pylint: disable=E1101
        return logging.getLogger(filename)

    logger = logging.getLogger(filename)
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)
    return logger
