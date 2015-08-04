
class Connection:
    def __init__(self,*args,**kwargs):
        self._host = kwargs.pop("host", "localhost")
        self._port = kwargs.pop("port", 9200)
