import pymysql
class DB(object):
    def __init__(self, **kw):
        self.__conn = pymysql.connect(
            host=kw['host'],
            port=kw['port'],
            user=kw['user'],
            password=kw['password'],
            database=kw['database'],
            charset='utf8'
        )
        if kw['dict'] is True:
            self.__cursor = self.__conn.cursor(pymysql.cursors.DictCursor)
        else:
            self.__cursor = self.__conn.cursor()