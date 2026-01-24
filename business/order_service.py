#order service - business layer
# A service class for handling order-related business logic.
# business/order_service.py
from business.models import Order, OrderItem


class OrderService:
    def __init__(self, order_repo, product_repo):
        self.order_repo = order_repo
        self.product_repo = product_repo
        self.order_id_counter = 1  # Automatically generate order IDs

    def create_order(self, user, cart_items):
        """
        Create a new order for a user.  Args:user (User): The user placing the order.
            cart_items (dict): A dict with product_id as keys and quantity as values.
        Returns: Order: The created order object.
        """
        items = []
        total_price = 0

        for product_id, qty in cart_items.items():
            # Find the product in the repository
            product = self.product_repo.find(product_id)
            if not product:
                raise ValueError(f"Product with ID {product_id} not found.")
            if product.stock < qty:
                raise ValueError(f"Insufficient stock for product '{product.name}'. Available stock: {product.stock}")

            # Deduct stock
            product.stock -= qty

            # Create and append OrderItem
            items.append(OrderItem(product_id=product_id, name=product.name, price=product.price, quantity=qty))
            total_price += product.price * qty

        # Create the order
        order = Order(order_id=self.order_id_counter, user=user.user_id, items=items)

        # Save order to the repository
        self.order_repo.save(order)
        self.order_id_counter += 1  # Increment order ID counter

        return order

    def get_orders_by_user(self, user_id):
        """
        Retrieve all orders by a specific user. Args: user_id (str): The ID of the user for whom to retrieve orders.
        Returns: ist(Order): List of orders associated with the given user_id.
        """
        return self.order_repo.get_orders_by_user(user_id)
