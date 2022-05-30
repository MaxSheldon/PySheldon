# -*- coding: utf-8 -*-

import os
import sys
import logging
from os import path
from datetime import datetime

class LogLevel:
    INFO = logging.INFO
    WARN = logging.WARN
    DEBUG = logging.DEBUG
    ERROR = logging.ERROR
    FATAL = logging.FATAL
    CRITICAL = logging.CRITICAL

class Log:
    def __init__(self,
                 file_name : str,
                 file_path : str = None,
                 print_log : bool = False,
                 log_format : str = None,
                 log_level : LogLevel = logging.INFO
                 ):
        if log_format is None:
            self.LOG_FORMAT = '[%(asctime)s] [%(levelname)s] [%(funcName)s] %(message)s'
        self.cria_file(file_name=file_name, file_path=file_path)
        self.PRINT_LOG = print_log
        self.LOG_LEVEL = log_level
        self.set_log()

    def cria_file(self, file_path : str, file_name : str) -> None:
        if file_path:
            if path.exists(path=file_path) is False:
                os.makedirs(file_path)
            self.FILE_NAME = path.join(file_path, file_name)
            return
        self.FILE_NAME = '{}'.format(file_name)

    def set_log(self) -> None:
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
    def get_date() -> str:
        return datetime.now().strftime('%Y-%d-%m')
