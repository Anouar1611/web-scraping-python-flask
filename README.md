# Full Stack web application using Flask and Scrapy Python

For this challenge, there are two popular libraries for scraping data from websites:

    1 - Beautiful Soup
    2 - Scrapy

`Scrapy` is a Web spider or framework for web scraping or crawling for crawling and fetching data from several websites.

> Web Crawling is used to extract data from websites where you program your crawler for crawling to web pages and downloading their contents.

- I choose `Scrapy` because it's more faster than others, used for large data, and used by the most popular search engine for providing a fast searching. So, Scrapy does many features you could probably need in your web scraping and other advantages, another reason for using `Scrapy` was for learning new and robust scraping frameworks.

In this challenge, I worked with Flask, SQLite, Unittest, Scrapy.

- Flask for build-up a web application in which you can click a button for scraping then the code of scraping is running and you will view your scraped data displayed on a web page.

- SQLite for storing the scraped data and retrieve these data from our SQLite database file.

- Unittest for make some small unit tests

- Scrapy for crawling web sites.

First, for building a Scrapy project you will have to set up a new startproject and run the following command :

```console 
scrapy startproject tutorial 
```
However, my project directory will be created with the following structure :

```console 
tutorial/
    scrapy.cfg            # it's a configuration file

    tutorial/             # prject module
        __init__.py

        items.py          # acts like the model

        middlewares.py    # it's for project middlwares, but I didn't use it

        pipelines.py      # it's for project pipelines, but I didn't use it

        settings.py       # project settings file

        spiders/          # in this directory you could add a specific spider for scraping
            __init__.py
```

Then, I start to develop my first spider which is a scraper for scraping data from specific websites wich is my ```ProductSpider``` class which extends from ```Spider``` class and then define my ```start_requests``` and ```parse``` for extracting data.

The following code is `ProductSpider` class :

```python
class ProductSpider(scrapy.Spider):
    name = "product"
    crudRepository = CRUDRepository()

    def start_requests(self):
        urls = [
            # my urls where I want to crawl or scrap from
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
```

After that, inside my ```app.py```, there are two routes :
 
* The first one is `/` in which Flask maps this URL to an index method and then executes this method which creates our database, select all items from this database, after render the template ```ìndex.html``` which is inside of my ***`templates`*** folder.

The following code is for the index method :

```python
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
```

The variable `rows` is for passing the data from my `index` class to `index.html` in which I displayed the scraped items. 

* The second one is `/` but with the method **POST**, Flask will execute the ``scrap_button`` method when you click the scrap button on the form in the ``index.html`` file. In this method, I used the `Process` module which is a module that gives the ability to use multiprocesses in your own machine and the `Reactor` module which is an event loop waits for then dispatches events or messages in a program and it blcoks until an event is occured, in our program the event is the ***ProductCrawler***. Moreover, if supposed that I didn't create an instance of Process module each time I click the scrap_button, then an Error will be raised because the reactor cannot be restarted, that's why I instantiate a Process object each time I click the scrap button for runing the reactor multiple times.

The following code for scrap_button method :

```python
@app.route('/', methods=['POST'])
def scrap_button():
    process = Process(target=func)
    process.start()
    process.join()

    return redirect(url_for('index'))

def func():
    runner = CrawlerRunner()
    deferred = runner.crawl(ProductSpider)
    deferred.addBoth(lambda _: reactor.stop())
    reactor.run()
```


Furthermore, I used the `Builder` design pattern because my `TutorialItem` model inside the `ìtems.py` `file contains many attributes, so the construction of my item will be more complex.


That's my TutorialItem class lokes like :

```python
class TutorialItem(scrapy.Item):

    # My fileds here

class AbstractBuilder():

    # provides an interface to create a tutorialItem object. It is only inherited by the ConcreteItemBuilder
 
class ConcreteItemBuilder(AbstractBuilder):

    # implements the AbstractBuilder and its methods, then it creates a tutorialItem object 
   
class Director():

    # Director is responsible to build and construct the tutorialItem object using an object of ConcreteItemBuilder 
    # Here I get my data from the HTML and CSS elments
```

However, I made all my CRUD operations inside a `DaoRepository` module for my interactions with the database in a `CRUDRepository` class inside `CRUDRepository.py` file which overrides methods in `CRUDInterface` interface. This class implements `CRUDInterface` interface inside `CrudInterface.py` file:

```python
class CRUDInterface():
    __metaclass__ = ABCMeta                                                     

    @abstractmethod
    def select(self):
        pass
    
    @abstractmethod
    def selectWhereURL(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def create(self):
        pass
```

For the connection with the database, I created a separate class which contains a `staticmethod` which establish the connection with our database, each time we need an interaction with it, I called `connect` method inside `connection.py` file.

Finally, I did some small unit tests for testing if my spider did the scraping well, these tests are included inside `testSpider.py` file.


>### Note1 : *To run the application, you will have to run the `app.py` file which is runned in the localhost:8081* 
