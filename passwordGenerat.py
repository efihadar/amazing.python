import random  
import string

def get_random_password_string(length):
    password_characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(password_characters) for i in range(length))

    print("Your Password is:", password)

get_random_password_string(12)