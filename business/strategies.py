"""implement a Strategy Pattern for flexible input validation. For example, having different
validation strategies for password strength (e.g., "basic" vs. "strong" validation rules)."""
# business/strategies.py
import string
from abc import ABC, abstractmethod

# Abstract Base Class for validation strategies
class PasswordValidationStrategy(ABC):
    # Abstract validate method that subclasses need to implement
    @abstractmethod
    def validate(self, password):
        """Validate the password."""
        pass

# Basic Validation Strategy
class BasicPasswordValidationStrategy(PasswordValidationStrategy):
    def validate(self, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit")

# Strong Validation Strategy
class StrongPasswordValidationStrategy(PasswordValidationStrategy):

    def __init__(self, min_length: int = 12):
        self.min_length = min_length
        self.special_chars = set(string.punctuation)

    def validate(self, password):
        if not isinstance(password, str):
            raise ValueError("Password must be a string")
        if len(password) < self.min_length:
            raise ValueError(f"Password must be at least {self.min_length} characters long")
        if not any(ch.isupper() for ch in password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(ch.islower() for ch in password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(ch.isdigit() for ch in password):
            raise ValueError("Password must contain at least one digit")
        if not any(ch in self.special_chars for ch in password):
            raise ValueError("Password must contain at least one special character")