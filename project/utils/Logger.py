__author__ = "Isaac Cárdenas"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Isaac Cárdenas"
__email__ = "is_cardenas@hotmail.com"
__status__ = "Development"
__date__ = "29/Agosto/2021"

import logging

class Logger():
    def __init__(self, LEVEL=logging.INFO):
        self.level = LEVEL
        self.logFormat = '[%(asctime)s.%(msecs)03d] - [%(process)d-%(name)s] - %(levelname)s - %(message)s'
        self.dateFormat = '%d-%b-%y %H:%M:%S'

    def getLogger(self, className):
        logging.basicConfig(format=self.logFormat, datefmt=self.dateFormat)
        logger = logging.getLogger(className)
        logger.setLevel(self.level)
        return logger
