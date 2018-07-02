from utils import database

USER_CHOICE = """

Welcome to the password management system.

Please enter you choice : 

'a' : to add a new password for your app
'l' : to list all the applications that you saved passwords for : 
'd' : to delete the password and it's corresponding application from the directory
'q' : to quit

Your choice : 

"""


def menu():
    database.create_password_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_password()

        elif user_input == 'l':
            prompt_list_passwords()

        elif user_input == 'd':
            prompt_delete_password()

        user_input = input(USER_CHOICE)


def prompt_add_password():
    user_application = input('Please enter the application for which the password should be saved : ')
    user_password = input('Please enter the password to be saved : ')
    database.add_password(user_application,user_password)


def prompt_list_passwords():
    passwords = database.list_passwords()
    if len(passwords) == 0:
        print('No saved passwords are available')
    for password in passwords:
        print(f"Password for application {password['application']} : {password['password']}")


def prompt_delete_password():
    application_to_be_deleted = input('Enter the application for which the password is to be deleted')
    database.delete_password(application_to_be_deleted)


menu()