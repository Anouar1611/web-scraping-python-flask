import scrapy
import sqlite3
import datetime

from scrapy.spiders import CrawlSpider
from ..items import TutorialItem,AbstractBuilder,ConcreteItemBuilder,Director
from ..connection import Connection
from ..DaoRepository.CrudRepository import CRUDRepository


class ProductSpider(scrapy.Spider):
    name = "product"
    crudRepository = CRUDRepository()

    def start_requests(self):
        urls = [
            'https://www.wollplatz.de/wolle/drops/drops-safran',
            'https://www.wollplatz.de/wolle/dmc/dmc-natura-xl',
            'https://www.wollplatz.de/wolle/stylecraft/stylecraft-special-dk',
            'https://www.wollplatz.de/wolle/drops/drops-baby-merino-mix'
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        concreteItemBuilder = ConcreteItemBuilder()
        director = Director(concreteItemBuilder)
        director.constructTutorialItem(response)
        
        item = director.getTutorialItem()
        rows = self.crudRepository.selectWhereURL(item)

        if len(rows) == 0:
            self.crudRepository.insert(item)
        else:
            self.crudRepository.update(item)
    
            

