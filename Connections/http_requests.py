from .base import Connection
from .utils import autoInitiator
class HttpRequests(Connection):
    @autoInitiator()
    def __init__(self,host="localhost",port=9200):
        pass
