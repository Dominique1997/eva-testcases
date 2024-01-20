import string
import random
class Generator():
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits

    @classmethod
    def generate_username(cls, min_len=5, max_len=5):
        random_len = random.randint(min_len, max_len)
        return ''.join(random.choices(cls.lowercase_letters + cls.numbers + cls.uppercase_letters, k=random_len))
    @classmethod
    def generate_password(cls, min_len=5, max_len=5):
        random_len = random.randint(min_len, max_len)
        return ''.join(random.choices(cls.lowercase_letters + cls.uppercase_letters + cls.numbers, k=random_len))
