from .base import Connection
from .utils import autoInitiator
import urllib3

class HttpUrllib3(Connection):

    @autoInitiator()
    def __init__(self,host="localhost",port="9200"):
        self._poolManager=urllib3.HTTPConnectionPool(self._host,port=self._port)



