import sqlite3


class Connection:

    @staticmethod
    def connect():
        return sqlite3.connect('products.db', check_same_thread = False)
        


