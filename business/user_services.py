#pg25304 UoEO service(Business Layer) - user Management
# hashlib provides hashing functions, such as sha256, which are used for securely hashing passwords.
import hashlib
#UserService, which contains the business logic for handling user-related operations like registration and login

class UserService:
    #It takes user_repo as an argument, which is an instance of UserRepository, so that UserService can interact with the user repository.
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def register(self, user_id, email, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        """A new User object is created, using the user_id, email, and the hashed password (password_hash).
Note: The User class must be defined elsewhere in the application for this to work."""
        user = User(user_id, email, password_hash)
        #This saves the newly created user object into
        # the repository using the save method from UserRepository.
        self.user_repo.save(user)
        #The register method returns the user object, allowing the caller to access the details of the registered user.
        return user
    # Login method to authenticate a user
    def login(self, email, password):
        #Find the user by email, using the find_by_email method from UserRepository.
        user = self.user_repo.find_by_email(email)
        if not user:
            #If user is None (no user found with the given email), the method immediately
            # returns False, indicating a login failure.
            return False
        #Hash the provided password to compare it with the stored password hash.
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        #Compare the hashed password with the stored password hash.
        return user.password_hash == password_hash








       #




"""password_hash = hashlib.sha256(password.encode()).hexdigest()
password.encode(): Converts the password string into bytes (required by hashlib).
hashlib.sha256(): Creates a sha256 digest of the password bytes.
.hexdigest(): Converts the resulting hash into a readable hexadecimal string."""