import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))

    for _ in range(num_passwords):
        password = generate_password(password_length)
        print("Generated Password:", password)

if _name_ == "_main_":
    main()