import unittest
from business.user_services import UserService
from business.models import User
from data.user_repository import UserRepository
from business.strategies import BasicPasswordValidationStrategy

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_repo = UserRepository()  # In-memory user repository
        self.password_strategy = BasicPasswordValidationStrategy()  # Basic password validation
        self.user_service = UserService(self.user_repo, self.password_strategy)

    def test_register_user(self):
        user = self.user_service.register(1, "test@example.com", "Test1234")
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.password_hash is not None)

    def test_register_user_invalid_email(self):
        with self.assertRaises(ValueError):
            self.user_service.register(1, "invalid-email", "Test1234")

    def test_login_user_success(self):
        self.user_service.register(1, "test@example.com", "Test1234")
        self.assertTrue(self.user_service.login("test@example.com", "Test1234"))

    def test_login_user_failure(self):
        # Register a user
        self.user_service.register(1, "test@example.com", "Test1234")
        # Try logging in with wrong password
        self.assertFalse(self.user_service.login("test@example.com", "WrongPass"))