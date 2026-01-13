"""Polymorphism allows you to swap repositories or add new ones that implement the same base
class without modifying the rest of the code. For example, we’ll add a TestUserRepository for testing:"""
from data.base_repository import BaseRepository

class TestUserRepository(BaseRepository):
    """A test repository for users."""
    def __init__(self):
        self.test_users = []  # Use a list for simple storage

    def save(self, user):
        """Save a user to the test storage."""
        self.test_users.append(user)

    def find(self, email):
        """Find user in the test storage."""
        for user in self.test_users:
            if user.email == email:
                return user
        return None