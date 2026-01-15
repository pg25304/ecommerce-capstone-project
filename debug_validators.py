from business.validators import validate_password

# Test validate_password directly
try:
    print("Testing valid password...")
    validate_password("ValidPass123")  # Should pass with no errors
    print("Valid password passed validation!")

    print("Testing short password...")
    validate_password("short")  # Should raise ValueError
except ValueError as e:
    print("Caught error:", e)