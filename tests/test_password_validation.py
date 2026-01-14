# Unit tests for password validation strategies
import unittest
from business.strategies import BasicPasswordValidationStrategy, StrongPasswordValidationStrategy

class TestPasswordValidationStrategies(unittest.TestCase):
    def test_basic_password_validation(self):
        strategy = BasicPasswordValidationStrategy()
        strategy.validate("P@ssw0rd")  # Should pass
        with self.assertRaises(ValueError):
            strategy.validate("short")  # Too short
        with self.assertRaises(ValueError):
            strategy.validate("password")  # No digit

    def test_strong_password_validation(self):
        strategy = StrongPasswordValidationStrategy()
        strategy.validate("StrongP@ssw0rd!")  # Should pass
        with self.assertRaises(ValueError):
            strategy.validate("Weak1!")  # Too short
        with self.assertRaises(ValueError):
            strategy.validate("Non#$pecial123")  # No special character

if __name__ == "__main__":
    unittest.main()