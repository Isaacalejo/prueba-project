__author__ = "Isaac Cárdenas"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Isaac Cárdenas"
__email__ = "is_cardenas@hotmail.com"
__status__ = "Development"
__date__ = "29/Agosto/2021"


import pandas_datareader as web
from datetime import datetime

from project.utils.Logger import Logger


class DataService:
    def __init__(self):
        self.__dateFormat = "%Y-%m-%d"
        self.log = Logger().getLogger(self.__class__.__name__)

    def getData(self, payload):
        ticker, start, end = self.__processPayload(payload)
        self.log.info(f"Consultando datos para ticker [{ticker}]")
        data = web.DataReader(ticker, 'yahoo', start, end)
        return data.to_json()

    def __processPayload(self, payload):
        ticker = payload.get("ticker", "MSFT")
        start = payload.get("start", "2017-1-1")
        end = payload.get("end", "2017-12-31")
        try:
            start = datetime.strptime(start, self.__dateFormat)
        except Exception as e:
            self.log.error(f"No se puede transformar la fecha de inicio [{start}]", e)
            start = datetime(2017, 1, 1)
        try:
            end = datetime.strptime(end, self.__dateFormat)
        except Exception as e:
            self.log.error(f"No se puede transformar la fecha de fin [{end}]", e)
            end = datetime(2017, 12, 31)
        return ticker, start, end
