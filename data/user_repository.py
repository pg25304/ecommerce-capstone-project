#pg25304 UoEO - Data Access Layer - User Repositories - user Management
#a container for methods that handle user-related operations. It provides functionality for saving and retrieving users.
from data.base_repository import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self):
        self.users = {}  # In-memory storage for users

    def save(self, user):
        self.users[user.user_id] = user

    def find(self, user_id):
        return self.users.get(user_id)

    def find_by_email(self, email):
        for user in self.users.values():
            if user.email == email:
                return user
        return None