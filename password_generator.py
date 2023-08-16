import string
import secrets
import random

print("Welcome to your random password generator!")

def generate_password():
    uppercase = int(input("How many uppercase letters do you want?"))
    lowercase = int(input("How many lowercase letters do you want?"))
    numbers = int(input("How many numbers do you want?"))
    special_characters = int(input("How many special characters do you want?"))
    password = ''

    for i in range(uppercase):
        password += ''.join(secrets.choice(string.ascii_uppercase))

    for i in range(lowercase):
        password += ''.join(secrets.choice(string.ascii_lowercase))

    for i in range(numbers):
        password += ''.join(secrets.choice(string.digits))

    for i in range(special_characters):
        password += ''.join(secrets.choice(string.punctuation))

    password = ''.join(random.sample(password, len(password)))

    print("Your password is " + password)

generate_password()
