"""
CP1404 - Password Checker
"""

MIN_LENGTH = 5


def main():
    user_password = get_password()
    password_asterisks(user_password)


def password_asterisks(user_password):
    for char in user_password:
        print("*", end="")


def get_password():
    user_password = input("Please enter password: ")
    while len(user_password) < MIN_LENGTH:
        print("Please enter a password with at least {} characters".format(MIN_LENGTH))
        user_password = input("Please enter password: ")
    return user_password


main()
