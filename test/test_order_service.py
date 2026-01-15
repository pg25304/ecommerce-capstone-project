import unittest
from business.order_service import OrderService
from data.order_repository import OrderRepository
from data.product_repository import ProductRepository
from business.models import Product, User

class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.order_repo = OrderRepository()
        self.product_repo = ProductRepository()
        self.order_service = OrderService(self.order_repo, self.product_repo)

        # Add a test product
        self.test_product = Product(product_id=1, name="Laptop", price=1000.0, stock=5)
        self.product_repo.save(self.test_product)

    def test_create_order_success(self):
        user = User(user_id=1, email="test@example.com", password_hash="hashed_pass")
        order = self.order_service.create_order(
            order_id=1, user=user, cart_items=[(1, 2)]  # Buy 2 laptops
        )
        self.assertEqual(order.order_id, 1)
        self.assertEqual(len(order.items), 1)  # One product in order
        self.assertEqual(order.items[0][1], 2)  # Quantity should be 2
        self.assertEqual(self.test_product.stock, 3)  # Stock reduced

    def test_create_order_insufficient_stock(self):
        user = User(user_id=1, email="test@example.com", password_hash="hashed_pass")
        with self.assertRaises(Exception):
            self.order_service.create_order(
                order_id=2, user=user, cart_items=[(1, 10)]  # Try to buy 10 laptops
            )