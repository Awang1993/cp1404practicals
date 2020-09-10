"""
CP1404 Practical
Emails
"""

EMAILS = {}


def main():
    user_email = input("Email: ")
    while user_email != "":
        user_name = user_email.split('@')
        if '.' in user_name:
            full_name = user_name[0].split('.')
            fullname = "{} {}".format(full_name[0], full_name[1]).title()
        else:
            fullname = user_name[0].title()
        name_check = input("Is your name {}? (y/n) ".format(fullname)).lower()
        # if name_check == 'n':
        #     new_name = input("Name: ")
        #     EMAILS[new_name.title()] = user_email
        else:
            EMAILS[fullname.title()] = user_email
        user_email = input("Email: ")
    for key, value in EMAILS.items():
        print("{} ({})".format(key, value))
    print(EMAILS)


main()
