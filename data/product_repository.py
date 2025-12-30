#product repository.py
#pg25304 UoEO - Data Access Layer - product catalog - product repository
#A repository class for managing product-related operations.
class ProductRepository:
    #The constructor method (__init__) is called when a new ProductRepository object is created.
    #It initializes the object, specifically the in-memory storage for products.
    def __init__(self):
        #In-memory storage for products
        self.products = {}
    #store a Product object in the repository.
    #It takes the product to be saved as an argument.
    def save(self, product):
        #Uses the product’s product_id as the key and the product object itself as the value.
        self.products[product.product_id] = product

    def find(self, product_id):
        return self.products.get(product_id)

    def list_all(self):
        return  list(self.products.values())


"""Summary:
ProductRepository Class:
This class manages an in-memory collection of Product objects.
Attributes:
self.products: A dictionary to store products, where the key is the product_id and the value is the Product object.
Methods:
save(product): Saves a Product object to the repository.
find(product_id): Retrieves a product by its product_id. Returns None if no product is found with the given ID.
list_all(): Returns a list of all stored Product objects.
This repository uses in-memory storage, making it suitable for applications with temporary data needs. For production
scenarios, this could be replaced with a database backend."""