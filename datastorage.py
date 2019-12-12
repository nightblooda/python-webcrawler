
import pymysql
import config
from pymysql import cursors

class sqloperater:
    def __init__(self, sqlstr):
        super().__init__()
        self.sqlstr = sqlstr
        self.status = ''
        
