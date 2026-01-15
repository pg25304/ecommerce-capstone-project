#order service - business layer
# A service class for handling order-related business logic.
# business/order_service.py
from business.models import Order
class OrderService:
    def __init__(self, order_repo, product_repo):
        self.order_repo = order_repo
        self.product_repo = product_repo

    def create_order(self, order_id, user, cart_items):
        items = []
        for product_id, qty in cart_items:
            product = self.product_repo.find(product_id)
            if product and product.stock >= qty:
                product.stock -= qty
                items.append((product, qty))
            else:
                raise Exception(f"Insufficient stock for product: {product.name if product else 'unknown'}")

        order = Order(order_id, user, items)
        self.order_repo.save(order)
        return order


"""Summary:
The constructor method (__init__) initializes the OrderService class.
It takes two parameters:
order_repo: An instance of the repository responsible for storing and managing orders.
product_repo: An instance of the repository responsible for managing products.
Assigns the order_repo parameter to the self.order_repo instance variable, allowing the OrderService class to save and retrieve orders.
Assigns the product_repo parameter to the self.product_repo instance variable, allowing the OrderService class to access and modify product details.
////////////////////
This defines a method named create_order to create an order.
It takes the following parameters:
order_id: A unique identifier for the new order.
user: The user who is placing the order.
cart_items: A list where each item is a tuple containing:
product_id: The ID of the product to be purchased.
qty: The quantity of the product to be purchased.
//////////////////
Initializes an empty list items, which will hold the products and their quantities that can be successfully added to the order.
Loops through each item in the cart_items list.
product_id is the ID of the product, and qty is the quantity the user wants to purchase.

Uses the find method of the product_repo to look up the product by its product_id.

Checks if:
product exists (i.e., it was successfully found in the repository).
The product has enough stock (product.stock) for the requested quantity (qty).

Reduces the product's stock by the quantity being purchased (qty), as the items will now be part of the order.

Adds a tuple (product, qty) to the items list, representing the product and the quantity being included in the order.

Creates a new Order object using:
order_id: The unique identifier for the order.
user: The user placing the order.
items: The list of products and their quantities.
The Order class would need to be defined elsewhere in the application.

Saves the newly created order into the repository using the save method of the order_repo.

Returns the newly created order object to the caller, so the application can continue processing or present the order details to the user.
//////////////////
Summary:
OrderService Class:

Handles the creation and management of orders.
Refers to two repositories:
product_repo: To retrieve and modify product stock.
order_repo: To save the newly created order.
create_order Method:

Loops through the cart_items and:
Checks if the products exist and if enough stock is available.
Reduces the product stock accordingly.
Adds the product and quantity to the items list for the order.
Creates an Order using the provided order_id, user, and items.
Saves the order in the order_repo and returns it."""
