# -*- coding: utf-8 -*-

import logging
from CommonLibrary.CommonConfiguration import result_path

class LogUtility(object):

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)


    def create_logger_file(self, filename):
        try:
            full_log_name = result_path()+'\\' + filename+'.log'
            fh = logging.FileHandler(full_log_name)
            fh.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s [line:%(lineno)d] %(message)s')
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
        except Exception as err:
            self.logger.debug("Error when creating log file, error message: {}".format(str(err)))


    def log(self, message):
        self.logger.debug(message)
