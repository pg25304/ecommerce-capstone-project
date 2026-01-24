# Unit tests for ProductService
import unittest
from business.product_service import ProductService
from data.product_repository import ProductRepository
from business.models import Product

class TestProductService(unittest.TestCase):
    def setUp(self):
        self.product_repo = ProductRepository()
        self.product_service = ProductService(self.product_repo)

    def test_add_product_success(self):
        # Add a product
        product = self.product_service.add_product("Laptop", 1500.0, 10)

        # Assert product details
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 1500.0)
        self.assertEqual(product.stock, 10)

        # Assert product ID generation
        self.assertEqual(product.product_id, 1)

    def test_add_product_invalid_price(self):
        # Add a product with negative price
        with self.assertRaises(ValueError) as context:
            self.product_service.add_product("Laptop", -1500.0, 10)
        self.assertEqual(str(context.exception), "Product name must not be empty, price must be greater than 0, and stock must not be negative.")

    def test_add_product_negative_stock(self):
        # Add a product with negative stock
        with self.assertRaises(ValueError) as context:
            self.product_service.add_product("Laptop", 1500.0, -10)
        self.assertEqual(str(context.exception), "Product name must not be empty, price must be greater than 0, and stock must not be negative.")

    def test_list_products(self):
        # Add products
        self.product_service.add_product("Laptop", 1500.0, 10)
        self.product_service.add_product("Phone", 800.0, 5)

        # Retrieve products
        products = self.product_service.list_products()
        self.assertEqual(len(products), 2)  # Assert that we have 2 products

        # Assert product details
        self.assertEqual(products[0].name, "Laptop")
        self.assertEqual(products[0].price, 1500.0)
        self.assertEqual(products[0].stock, 10)

        self.assertEqual(products[1].name, "Phone")
        self.assertEqual(products[1].price, 800.0)
        self.assertEqual(products[1].stock, 5)