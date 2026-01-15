import unittest
from business.validators import validate_email, validate_password

class TestValidators(unittest.TestCase):
    def test_validate_email(self):
        # Valid email
        self.assertIsNone(validate_email("valid@example.com"))  # Should pass
        # Invalid emails
        with self.assertRaises(ValueError):
            validate_email("invalid-email")
        with self.assertRaises(ValueError):
            validate_email("")

    def validate_password(password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(char.islower() for char in password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit")
        if any(char.isspace() for char in password):  # Check for spaces
            raise ValueError("Password must not contain spaces")






""" def test_validate_password(self):
        print("TEST: Validate password with strong and weak cases...")

        # Valid cases
        self.assertIsNone(validate_password("ValidPass123"), "Failed on valid password: 'ValidPass123'")
        self.assertIsNone(validate_password("A1bcdeFg"), "Failed on valid password: 'A1bcdeFg'")

        # Edge case: Minimum 8 characters (boundary case)
        with self.assertRaises(ValueError, msg="Failed to catch error: too short password"):
            validate_password("Short1")  # Too short (7 characters)
        self.assertIsNone(validate_password("A1bcdefg"), "Failed on minimum valid password: 'A1bcdefg'")

        # Invalid cases
        with self.assertRaises(ValueError, msg="Failed to catch error: no uppercase letter"):
            validate_password("nocapital123")
        with self.assertRaises(ValueError, msg="Failed to catch error: no lowercase letter"):
            validate_password("NOLOWER123")
        with self.assertRaises(ValueError, msg="Failed to catch error: no digit"):
            validate_password("NoDigitsHere")

        # Edge case: Disallow spaces
        with self.assertRaises(ValueError, msg="Failed to catch error: spaces in password"):
            validate_password("Valid Pass123")  # Spaces in password"""