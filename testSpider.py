import unittest
from tutorial.DaoRepository.CrudRepository import CRUDRepository
from tutorial.spiders.product_spider import ProductSpider

URL = "https://www.wollplatz.de/wolle/drops/drops-baby-merino-mix"
WRONG_URL = "https://www.google.com"
EXPECTED_PRICE_BY_URL = 2.72
EXPECTED_PRICE = ('8,05',)
WRONG_EXPECTED_PRICE = ('10.67',)
EXPECTED_RESULT = 1
EXPECTED_WRONG_RESULT = 0

class TestSpider(unittest.TestCase):

    def test_price_exist_by_url(self):
        crudRepository = CRUDRepository()
        crudRepository.create()
        sum1=crudRepository.selectByUrl(URL)
        self.assertEqual(sum1, str(EXPECTED_PRICE_BY_URL), "Shloud be 2.72")

    def test_price_if_exist(self):
        crudRepository = CRUDRepository()
        crudRepository.create()
        self.assertEqual(crudRepository.selectByPrice().count(EXPECTED_PRICE), EXPECTED_RESULT, "Shloud be 1")
    
    def test_price_if_not_exist(self):
        crudRepository = CRUDRepository()
        crudRepository.create()
        self.assertEqual(crudRepository.selectByPrice().count(WRONG_EXPECTED_PRICE), EXPECTED_WRONG_RESULT, "Shloud be 0")
    

if __name__ == '__main__':
    unittest.main()