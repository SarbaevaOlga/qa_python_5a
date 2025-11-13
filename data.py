import random
import string

class UserCredentials:
    USERNAME = "SarbaevaOlga"
    EMAIL = "sarbaeva_olga32@rambler.com"
    PASSWORD = "secure_password_123"

class TestUserData:
    @staticmethod
    def generate_username():
        return f"TestUser{random.randint(1000, 9999)}"
    
    @staticmethod
    def generate_email():
        return f"test{random.randint(1000, 9999)}@example.com"
    
    @staticmethod
    def generate_password():
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(8))