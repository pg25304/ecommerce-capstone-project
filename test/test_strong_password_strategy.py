import unittest
from business.strategies import StrongPasswordValidationStrategy

class TestStrongPasswordStrategy(unittest.TestCase):
    def setUp(self):
        self.strategy = StrongPasswordValidationStrategy()

    def test_valid_password(self):
        # Valid strong password - should pass
        self.strategy.validate("Str0ng@Password!")  # Should pass

    def test_too_short(self):
        # Invalid - Fails due to length < 12
        with self.assertRaises(ValueError, msg="Failed to catch error: too short password"):
            self.strategy.validate("Short1!")

    def test_no_uppercase(self):
        # Invalid - Fails due to missing uppercase letter
        with self.assertRaises(ValueError, msg="Failed to catch error: no uppercase letter"):
            self.strategy.validate("nouppercase1!")

    def test_no_special_character(self):
        # Invalid - Fails due to missing special character
        with self.assertRaises(ValueError, msg="Failed to catch error: no special character"):
            self.strategy.validate("NoSpecial123")

    def test_no_digits(self):
        # Invalid - Fails due to missing digits
        with self.assertRaises(ValueError, msg="Failed to catch error: no digit"):
            self.strategy.validate("NoSpecial!")

    def test_no_lowercase(self):
        # Invalid - Fails due to missing lowercase letter
        with self.assertRaises(ValueError, msg="Failed to catch error: no lowercase letter"):
            self.strategy.validate("NOLOWERCASE1!")

if __name__ == "__main__":
    unittest.main()