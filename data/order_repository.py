#order repository - data access layer
# A repository class for managing order-related operations.
from data.base_repository import BaseRepository
class OrderRepository(BaseRepository):
    def __init__(self):
        # In-memory storage for orders
        self.orders = {}

    def save(self, order):
        # Saves an Order object to the repository.
        self.orders[order.order_id] = order

    def find(self, order_id):
        """Finds an order by ID."""
        return self.orders.get(order_id) 