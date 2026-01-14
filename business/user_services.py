#pg25304 UoEO service(Business Layer) - user Management
# hashlib provides hashing functions, such as sha256, which are used for securely hashing passwords.
import bcrypt
from business.models import User
from business.validators import validate_email, validate_password
from business.strategies import PasswordValidationStrategy
#UserService, which contains the business logic for handling user-related operations like registration and login

class UserService:
    def __init__(self, user_repo, password_validation_strategy: PasswordValidationStrategy): #dependency injection
        self.user_repo = user_repo
        self.password_validation_strategy = password_validation_strategy #inject strategy here

    def register(self, user_id, email, password):
        validate_email(email)  # Validate email format
        self.password_validation_strategy.validate(password)  # Use password strategy

        # Hash and save user as before
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User(user_id, email, password_hash)
        self.user_repo.save(user)
        return user

    # Login method to authenticate a user
    def login(self, email, password):
        #Find the user by email, using the find_by_email method from UserRepository.
        user = self.user_repo.find_by_email(email)
        if not user:
            #If user is None (no user found with the given email), the method immediately
            # returns False, indicating a login failure.
            return False

        # Verify password using bcrypt's checkpw method
        return bcrypt.checkpw(password.encode(), user.password_hash.encode())








       #




"""password_hash = hashlib.sha256(password.encode()).hexdigest()
password.encode(): Converts the password string into bytes (required by hashlib).
hashlib.sha256(): Creates a sha256 digest of the password bytes.
.hexdigest(): Converts the resulting hash into a readable hexadecimal string."""