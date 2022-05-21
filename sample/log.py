# -*- coding: utf-8 -*-

import sys
import logging
from datetime import datetime

class LogLevel:
    INFO = logging.INFO
    WARN = logging.WARN
    DEBUG = logging.DEBUG
    ERROR = logging.ERROR
    FATAL = logging.FATAL
    CRITICAL = logging.CRITICAL

class Log:
    def __init__(self, file_name, print_log=False, log_format=None, log_level=logging.INFO):
        if log_format is None:
            self.LOG_FORMAT = '%(asctime)s | %(levelname)s | %(funcName)s | %(message)s'
        self.FILE_NAME = file_name
        self.PRINT_LOG = print_log
        self.LOG_LEVEL = log_level
        self.set_log()

    def set_log(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(level=self.LOG_LEVEL)

        formater = logging.Formatter(self.LOG_FORMAT)

        file_handler = logging.FileHandler(filename=self.FILE_NAME, encoding='utf-8')
        file_handler.setLevel(level=self.LOG_LEVEL)
        file_handler.setFormatter(fmt=formater)

        file_handler = logging.FileHandler(filename=self.FILE_NAME, encoding='utf-8')
        file_handler.setLevel(level=self.LOG_LEVEL)
        file_handler.setFormatter(fmt=formater)

        stdout_handler = logging.StreamHandler(stream=sys.stdout)
        stdout_handler.setLevel(level=self.LOG_LEVEL)
        stdout_handler.setFormatter(fmt=formater)

        self.logger.addHandler(file_handler)
        if self.PRINT_LOG: self.logger.addHandler(stdout_handler)

    @staticmethod
    def get_date():
        return datetime.now().strftime('%Y-%d-%m')
