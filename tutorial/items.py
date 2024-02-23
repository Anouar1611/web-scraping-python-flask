# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime

INDEX = -1
INDEX_DELIVERY_TIME = -2
IMAGE_ELEMENT = "#ContentPlaceHolder1_upPanelPhotos .pdetail-fullscreen img::attr(src)"
PRICE_ELEMENT = ".product-price .product-price-amount::text"
DELIVERY_TIME_ELEMENT = "#actie-bar-2 a::text"
NEEDLE_SIZE_ELEMENT = "tr:nth-child(4) td+ td::text"
COMPOSITION = "tr:nth-child(3) td+ td::text"

class TutorialItem(scrapy.Item):

    url = scrapy.Field()
    name = scrapy.Field()
    image = scrapy.Field()
    price = scrapy.Field()
    delivery_time = scrapy.Field()
    needle_size = scrapy.Field()
    composition = scrapy.Field()
    last_updated = scrapy.Field()


class AbstractBuilder():
    def __init__(self):
        self.item = None
    def createNewTutorialItem(self):
        self.item = TutorialItem()
 
class ConcreteItemBuilder(AbstractBuilder):
    def add_url(self, url):
        self.item ['url'] = url
    def add_name(self, name):
        self.item ['name'] = name
    def add_image(self, image):
        self.item ['image'] = image
    def add_price(self, price):
        self.item ['price'] = price
    def add_delivery_time(self, delivery_time):
        self.item ['delivery_time'] = delivery_time
    def add_needle_size(self, needle_size):
        self.item ['needle_size'] = needle_size
    def add_composition(self, composition):
        self.item ['composition'] = composition
    def add_last_updated(self, last_updated):
        self.item ['last_updated'] = last_updated
   
class Director():
    
    def __init__(self, builder):
        self._builder = builder

    def constructTutorialItem(self, response):
        self._builder.createNewTutorialItem()
        self._builder.add_url(response.url)
        self._builder.add_name(' '.join(map(lambda word: word.capitalize(), response.url.split("/")[INDEX].split('-'))))
        self._builder.add_image(response.css(IMAGE_ELEMENT).get())
        self._builder.add_price(response.css(PRICE_ELEMENT).get())
        self._builder.add_delivery_time(response.css(DELIVERY_TIME_ELEMENT).get().split(" ")[INDEX_DELIVERY_TIME])
        self._builder.add_needle_size(response.css(NEEDLE_SIZE_ELEMENT).get())
        self._builder.add_composition(response.css(COMPOSITION).get())
        self._builder.add_last_updated(datetime.datetime.now())

    def getTutorialItem(self):
        return self._builder.item





    

