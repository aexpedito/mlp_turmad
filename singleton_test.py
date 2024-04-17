
class MySQLDB:

    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

class MySQLDBClient:

    _conn = None
    def __init__(self):
        self._conn = MySQLDB.instance()
    def get_conn(self):
        return self._conn

    def run_select(self, query):
        pass

if __name__ == '__main__':

    client = MySQLDBClient()
    client.run_select("select ..")
