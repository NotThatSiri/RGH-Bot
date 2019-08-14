# coding=utf-8
import logging

class DefaultLogging:
    LoggingLevel = logging.INFO

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(LoggingLevel)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)


def get_logger(name, handler=DefaultLogging.ch):
    logger = logging.getLogger(name)
    logger.setLevel(DefaultLogging.LoggingLevel)
    logger.addHandler(handler)
    return logger
