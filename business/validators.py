# business/validators.py
import re
import html

def sanitize_input(input_value):
    """Escape special characters to prevent injection-based attacks."""
    return html.escape(input_value)
# Validate email format
def validate_email(email):
    email = sanitize_input(email)  # Sanitize before validation
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise ValueError("Invalid email format")
# Validate password strength
def validate_password(password):
    # Ensure password is strong enough
    print("DEBUG: validate_password() called with:", password)  # Debug Statement
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter")
    if not any(char.islower() for char in password):
        raise ValueError("Password must contain at least one lowercase letter")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit")