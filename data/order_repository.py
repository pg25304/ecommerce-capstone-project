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

    def get_orders_by_user(self, user_id):
        """
        Retrieves all orders placed by a specific user.Args:user_id (str): The ID of the user.
        Returns:list: A list of Order objects for the specified user ID.
        """
        return [order for order in self.orders.values() if order.user == user_id]