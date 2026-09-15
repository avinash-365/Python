import random
import string

def generate_random_number(start, end):
    return random.randint(start, end)

def generate_random_list(size, start, end):
    random_list = []
    for _ in range(size):
        random_list.append(random.randint(start, end))
    return random_list

def create_random_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def generate_random_otp(digits=6):
    otp = ""
    for _ in range(digits):
        otp += str(random.randint(0, 9))
    return otp