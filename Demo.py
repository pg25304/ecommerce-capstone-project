#demo of an e-commerce application using layered architecture
from data.user_repository import UserRepository
from data.product_repository import ProductRepository
from data.order_repository import OrderRepository

from business.user_services import UserService
from business.product_service import ProductService
from business.order_service import OrderService

from presentation.user_controller import UserController
from business.strategies import StrongPasswordValidationStrategy

# Setup repositories
user_repo = UserRepository()
product_repo = ProductRepository()
order_repo = OrderRepository()

# Setup services
user_strategy = StrongPasswordValidationStrategy()  # Use strong password rules for users
user_service = UserService(user_repo, user_strategy)
product_service = ProductService(product_repo)
order_service = OrderService(order_repo, product_repo)

# Setup controllers
user_controller = UserController(user_service)

# Demonstration of the Application
if __name__ == "__main__":
    print("Welcome to the E-commerce App Demo!")
    print("===================================")

    # User Registration
    print("\nStep 1: Register a User")
    user_id = input("Enter a user ID: ")  # Added user_id input
    email = input("Enter a valid email address: ")  # Changed variable from username to email
    password = input("Enter a password: ")
    try:
        registration_result = user_controller.register_user(user_id, email, password)
        print(f"{registration_result}")
    except ValueError as e:
        print(f"Failed to register user: {e}")

    # Display the hashed password for demonstration purposes
    print(f"\nAfter registration, the password for {email} is securely stored as:")
    user_data = user_repo.find_by_email(email)  # Assuming find_by_email is implemented
    if user_data:
        print(user_data.password_hash)
    else:
        print("Error: Could not find the user in the database after registration!")
    # User Login
    print("\nStep 2: User Login")
    email = input("Enter your email to login: ")
    password = input("Enter your password: ")
    try:
        login_result = user_controller.login_user(email, password)
        print(login_result)
    except ValueError as e:
        print(f"Login failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during login: {e}")

    # Add Products to the store
    print("\nStep 3: Add Products to the Store")
    while True:
        product_name = input("Enter product name (or type 'done' to finish): ").strip()
        if product_name.lower() == 'done':
            break
        product_price = float(input(f"Enter price for '{product_name}': $"))
        product_stock = int(input(f"Enter stock for '{product_name}': "))
        try:
            # Pass only name, price, and stock since product ID is automatically generated
            product = product_service.add_product(product_name, product_price, product_stock)
            print(
                f"Successfully added: Product[ID: {product.product_id}, Name: {product.name}, Price: ${product.price}, Stock: {product.stock}]")
        except ValueError as e:
            print(f"Error: {e}")

    # View All Products
    print("\nStep 4: View All Products")
    products = product_service.list_products()  # Fetch all products from the repository
    if products:
        print("\nAvailable Products:")
        for product in products:
            print(f"ID: {product.product_id}, Name: {product.name}, Price: ${product.price}, Stock: {product.stock}")
    else:
        print("No products are available in the store. Please add some.")

    # Place an Order
    print("\nStep 5: Place an Order")
    cart_items = {}  # Dictionary to store product ID and quantity

    # Allow the user to create their cart by adding products and quantities
    while True:
        product_id = input("Enter Product ID to add to your cart (or type 'done' to complete your order): ").strip()
        if product_id.lower() == 'done':  # When the user finishes adding items
            break

        if not product_id.isdigit():
            print("Invalid input. Please enter a valid numerical Product ID.")
            continue
        product_id = int(product_id)

        product_quantity = input(f"Enter the quantity for Product ID {product_id}: ").strip()
        if not product_quantity.isdigit():
            print("Invalid input. Please enter a valid quantity.")
            continue
        product_quantity = int(product_quantity)

        # Add product_id and quantity to the cart_items dictionary
        if product_id in cart_items:
            cart_items[product_id] += product_quantity  # Increment quantity
        else:
            cart_items[product_id] = product_quantity

    print("\nCart Items Added:")
    for product_id, qty in cart_items.items():
        print(f"Product ID: {product_id}, Quantity: {qty}")

    # Retrieve the full user object first (from the user_repo)
    user = user_repo.find_by_email(email)  # Use the email of the logged-in user
    if not user:
        print("Error: User not found!")
    else:
        try:
            # Create order using the full user object and cart_items
            order = order_service.create_order(user, cart_items)
            print(f"\nOrder successfully created! Your Order ID is: {order.order_id}")
            print("\nOrder Details:")
            for item in order.items:
                print(f"- {item.name}: {item.quantity} x ${item.price} = ${item.quantity * item.price}")
            print(f"Total Order Price: ${order.total_price():.2f}")
        except Exception as e:
            print(f"Could not create the order: {e}")


    # View Order History
    print("\nStep 6: View User Order History")

    # Fetch all orders for the logged-in user
    user_orders = order_service.get_orders_by_user(user_id)

    if user_orders:
        print(f"\nOrder History for User '{user_id}':")
        for order in user_orders:
            print(f"\nOrder ID: {order.order_id}, Total Price: ${order.total_price():.2f}")
            print("Items in this order:")
            for item in order.items:
                print(f"- {item.name}: {item.quantity} x ${item.price} = ${item.quantity * item.price}")
    else:
        print("No orders found for this user.")