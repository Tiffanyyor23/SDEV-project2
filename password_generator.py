"""
The purpose of the module is to provide the functions of a
password generator for the user.
"""


import string
import secrets
from verification import check_if_value_is_alpha, check_value_range


password_generator_options = {
    "a": "Letters Only",
    "b": "Numbers Only",
    "c": "Alphanumeric"}


def generate_alpha_only(length):
    alphabet = string.ascii_letters
    password = ''.join(secrets.choice(alphabet) for i in range(int(length)))
    print(f'Below is your generated password: \n {password}')
    print("Good Bye.")


def generate_number_only(length):
    alphabet = string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(int(length)))
    print(f'Below is your generated password: \n {password}')
    print("Good Bye.")


def generate_alphanumeric_only(length):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(int(length)))
    print(f'Below is your generated password: \n {password}')
    print("Good Bye.")


def main():
    print("You have selected to generate a password.")
    password_length = check_value_range(input("Please enter a value, between and including 8 - 64, for "
                                              "the password length: "))
    print("Please select the letter associated with the selection you would like to choose.")
    for password_choice, password_option in password_generator_options.items():
        print(f'{password_choice} : {password_option}')
    password_selection = check_if_value_is_alpha(input("Selection: "), 1)
    print(password_selection)
    if password_selection == "a":
        generate_alpha_only(password_length)
    elif password_selection == "b":
        generate_number_only(password_length)
    elif password_selection == "c":
        generate_alphanumeric_only(password_length)

