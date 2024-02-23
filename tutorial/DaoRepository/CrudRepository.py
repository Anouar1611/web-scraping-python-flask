
from CrudInterface import CRUDInterface
from ..items import TutorialItem
from ..connection import Connection

NAME = "name"
URL = "url"
PRICE = "price"
DELIVERY_TIME = "delivery_time"
NEEDLE_SIZE = "needle_size"
IMAGE = "image"
COMPOSITION = "composition"
LAST_UPDATE = "last_update"
PRODUCT_TABLE = "product_details"

class CRUDRepository(CRUDInterface):
    

    conn = Connection.connect()

    def select(self):
        c=self.conn.cursor()
        c.execute("SELECT * FROM " +PRODUCT_TABLE+ "")
        return c.fetchall()

    def selectWhereURL(self, item):
        c=self.conn.cursor()
        c.execute("SELECT id FROM " +PRODUCT_TABLE+ " WHERE " +URL+ " = ?", (item[URL],))
        return c.fetchall()
    
    def insert(self, item):
        c = self.conn.cursor()
        query = '''
                INSERT INTO '''+PRODUCT_TABLE+''' (''' +URL+ ''', ''' +NAME+ ''', ''' +PRICE+ ''', ''' +DELIVERY_TIME+ ''', ''' +NEEDLE_SIZE+ ''', ''' +COMPOSITION+ ''', ''' +IMAGE+ ''', ''' +LAST_UPDATE+ ''')
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        c.execute(query, (item[URL], item[NAME], item[PRICE], item[DELIVERY_TIME], item[NEEDLE_SIZE], item[COMPOSITION], item[IMAGE], item['last_updated']))
        self.conn.commit()
    
    def update(self, item):
        c = self.conn.cursor()
        query = '''
                UPDATE '''+PRODUCT_TABLE+'''
                SET ''' +NAME+ '''=?, ''' +PRICE+ '''=?, ''' +DELIVERY_TIME+ '''=?, ''' +NEEDLE_SIZE+ '''=?, ''' +COMPOSITION+ '''=?, ''' +IMAGE+ '''=?, ''' +LAST_UPDATE+ '''=?
                WHERE ''' +URL+ '''=?
        '''
        c.execute(query, (item[NAME], item[PRICE], item[DELIVERY_TIME], item[NEEDLE_SIZE], item[COMPOSITION], item[IMAGE], item[URL], item['last_updated']))
        self.conn.commit()

    def create(self):
        self.conn.text_factory = str
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS '''+PRODUCT_TABLE+''' (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ''' +URL+ ''' TEXT,
                ''' +NAME+ ''' TEXT,
                ''' +PRICE+ ''' REAL,
                ''' +DELIVERY_TIME+ ''' INTEGER,
                ''' +NEEDLE_SIZE+ ''' INTEGER,
                ''' +COMPOSITION+ ''' TEXT,
                ''' +IMAGE+ ''' TEXT,
                ''' +LAST_UPDATE+ ''' TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def selectByUrl(self, urlTest):
        c=self.conn.cursor()
        c.execute("SELECT price FROM " +PRODUCT_TABLE+ " where url = '" +urlTest+ "'")
        somme=c.fetchone()
        return somme[0].replace(",",".")
    
    def selectByPrice(self):
        c=self.conn.cursor()
        c.execute("SELECT price FROM " +PRODUCT_TABLE+ "")
        return c.fetchall()
    



