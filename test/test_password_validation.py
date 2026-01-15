# Unit test for password validation strategies
# python
# Unit test for password validation strategies
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
            strategy.validate("Wek!")  # Too short
        with self.assertRaises(ValueError):
            strategy.validate("Npeal122gh")  # No special character

if __name__ == "__main__":
    unittest.main()
