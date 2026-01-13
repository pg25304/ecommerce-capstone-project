#pg25304 UoEO Dec 2025 Controller (presentation layer) for user-related operations
"""This defines a class named UserController, which acts as a bridge between the external interface
 (e.g., web or UI layer) and the business logic in UserService."""
class UserController:
    #initializes the UserController class.
    # takes user_service as a parameter, which is an instance of UserService.
        def __init__(self, user_service):
            self.user_service = user_service
    #This defines a method named register_user, which acts as a controller action for user registration.
    #It takes user_id, email, and password as input parameters coming from the external interface (UI, API, etc.)."""
        def register_user(self, user_id, email, password):
            try:
                #This method calls the register_user method of UserService,
                return self.user_service.register(user_id, email, password)
            except ValueError as e:
                return f"Registration failed: {e}"  # Handle input validation errors
            except Exception as e:
                return f"Unexpected error: {e}"  # Handle unexpected issues


    #This calls the register method of UserService, passing the user_id, email, and password.
    #The result (the registered User object) is returned to the caller (e.g., API or UI).
    #UserService handles the actual business logic for registering the user.
        def login_user(self, email, password):

            try:
                if self.user_service.login(email, password):
                    return f"Login successful for {email}"
                else:
                    return "Invalid email or password"
            except Exception as e:
                return f"Login error: {e}"


#This calls the login method of UserService, passing the email and password.
#The result (True for successful login or False for a failed login) is returned to the caller (e.g., API or UI).
#UserService handles the actual business logic for authenticating the user.
#Summary:
#UserController Class:
#Provides an interface (methods) for external layers (UI, API, etc.) to interact with the application logic.
#Delegates the actual work to UserService for:
#User registration (register_user) → Calls UserService.register.
#User login (login_user) → Calls UserService.login.
#The UserController acts as a thin layer that connects
#external requests (e.g., from APIs or the UI) to the business logic encapsulated in the UserService.
#It does minimal processing itself and relies on UserService for the heavy lifting."""