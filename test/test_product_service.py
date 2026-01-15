import unittest
from business.product_service import ProductService
from data.product_repository import ProductRepository

class TestProductService(unittest.TestCase):
    def setUp(self):
        self.product_repo = ProductRepository()
        self.product_service = ProductService(self.product_repo)

    def test_add_product(self):
        product = self.product_service.add_product(1, "Laptop", 1500.0, 10)
        self.assertEqual(product.product_id, 1)
        self.assertEqual(product.name, "Laptop")

    def test_get_product(self):
        self.product_service.add_product(1, "Laptop", 1500.0, 10)
        product = self.product_service.get_product(1)
        self.assertEqual(product.name, "Laptop")

    def test_list_products(self):
        self.product_service.add_product(1, "Laptop", 1500.0, 10)
        self.product_service.add_product(2, "Phone", 800.0, 20)
        products = self.product_service.list_products()
        self.assertEqual(len(products), 2)