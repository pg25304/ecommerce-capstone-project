#order repository - data access layer
# A repository class for managing order-related operations.
class OrderRepository:
    def __init__(self):
        # In-memory storage for orders
        self.orders = {}

    def save(self, order):
        # Saves an Order object to the repository.
        self.orders[order.order_id] = order