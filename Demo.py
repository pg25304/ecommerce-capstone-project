from data.user_repository import UserRepository
from data.product_repository import ProductRepository
from data.order_repository import OrderRepository

from business.user_services import UserService
from business.product_service import ProductService
from business.order_service import OrderService

from presentation.user_controller import UserController

#setup repositories
user_pro = UserRepository()
product_repo = ProductRepository()
order_repo = OrderRepository()

#setup services
user_service = UserService(user_pro)
product_service = ProductService(product_repo)
order_service = OrderService(order_repo, product_repo)

#setup controllers
user_controller = UserController(user_service)

# python
# In `Demo.py` replace the registration block with this
try:
    new_user = user_service.register(1, "jack@example.com", "securepassword")
except ValueError as e:
    print("User registration failed:", e)
    import sys
    sys.exit(1)

# extra sanity check in case the service returns an error message string
if new_user is None or isinstance(new_user, str):
    print("User registration failed:", new_user)
    import sys
    sys.exit(1)

# proceed to create the order using the real User object
order = order_service.create_order(
    order_id=5001,
    user=new_user,
    cart_items=[(101, 1), (102, 2)]
)


print("Order created for:", order.user.email)
for product, qty in order.items:
    print(f"- {product.name} x{qty}")
