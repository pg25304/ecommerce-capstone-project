#pg25304 UoEO - Data Access Layer - User Repositories - user Management
#a container for methods that handle user-related operations. It provides functionality for saving and retrieving users.
class UserRepository:
    #The constructor method (__init__) is automatically called when an object of UserRepository is created. It initializes the object.
    def __init__(self):
        #This dictionary acts as simple in-memory storage where users are stored with their user_id as the key and the user object as the value.
        self.users = {} # In-memory storage for users

    def save(self, user):
        #This method takes a user object as an argument and saves it to the users dictionary using the user_id as the key.
        self.users[user.user_id] = user

    def find_by_email(self, email):
        #This method searches for a user by their email address. It iterates through the users dictionary and returns the user object if a match is found;
        # otherwise, it returns None.
        for user in self.users.values():
            if user.email == email:
                return user
        return None