from flask import Flask, render_template, redirect, url_for
from scrapy.crawler import CrawlerRunner,CrawlerProcess
from tutorial.spiders.product_spider import ProductSpider
from tutorial.spiders.product2_spider import ProductSpider2

from multiprocessing import Process, Queue
from twisted.internet import reactor, defer
import sqlite3
import datetime
from tutorial.connection import Connection
from tutorial.DaoRepository.CrudRepository import CRUDRepository


crawler_process = CrawlerRunner()
app = Flask(__name__)



@app.route('/')
def index():
    crudRepository1 = CRUDRepository()
    crudRepository1.create()
    rows = crudRepository1.select()

    my_rows = []
    for row in rows:
        my_row = list(row)
        dt = datetime.datetime.strptime(row[8], "%Y-%m-%d %H:%M:%S.%f")
        my_row[8] = datetime.datetime.strftime(dt ,"%b %d, %Y at %H:%M")
        my_rows.append(tuple(my_row))

    return render_template('index.html', rows=my_rows)

@app.route('/', methods=['POST'])
def scrap_button():
    # runner = CrawlerRunner()
    # def printTime():
    #     runner.crawl(ProductSpider)
    #     print("Current 1")

    # def printTime2():
    #     runner.crawl(ProductSpider2)
    #     print("Current 2")
    # process = CrawlerProcess()
    # process.crawl(ProductSpider)
    process = Process(target=func)
    # @defer.inlineCallbacks
    # def crawl():
    #     yield runner.crawl(ProductSpider) 
    #     yield runner.crawl(ProductSpider2)
    #     reactor.stop()

    # crawl()
    # reactor.run()
    
    # reactor.callLater(1,printTime2)
    # reactor.callLater(2,printTime)

    # deferred = runner.join()
    
    # deferred.addBoth(lambda _: reactor.stop())
    # reactor.run()
    process.start()
    process.join()

    return redirect(url_for('index'))

def func():
    runner = CrawlerRunner()
    deferred = runner.crawl(ProductSpider)
    deferred.addBoth(lambda _: reactor.stop())
    reactor.run()
       

if __name__ == '__main__':
    app.run(host='localhost', port='8081', debug=True)



