class ResponseWrapper:

    def __init__(self, ok, status, data):
        self.ok = ok
        self.status = status
        self.data = data

    @property
    def ok(self):
        return self._ok

    @property
    def status(self):
        return self._status

    @property
    def data(self):
        return self._data

    @ok.setter
    def ok(self, ok):
        self._ok = ok

    @status.setter
    def status(self, status):
        self._status = status

    @data.setter
    def data(self, data):
        self._data = data