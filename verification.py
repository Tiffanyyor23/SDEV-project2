"""
The purpose of this module is to define functions for checking the value of
user input.

"""


def check_if_value_is_alpha(value, length):
    # This function ensures the input is a single character letter.
    while (len(value) > length and (not value.isalpha())) or (len(value) > length and value.isalpha()) \
            or (not value.isalpha()):
        # while the value is not alpha and the length of value is not greater than the length provided.
        value = input("The value you provided is not valid.  \nPlease only enter a"
                      " single letter corresponding to the provided selection: ")
    return value


def check_if_value_is_numeric(value):
    # This function ensures the value is numeric and presented as a integer.
    while not value.isnumeric():
        value = input("The value you provided is not valid.  Please enter a numeric value")
    return int(value)


def check_value_range(value):
    # This function checks that a numeric value is in a specified range.
    while check_if_value_is_numeric(value) not in range(8, 65):
        value = input("The value you provided is not valid.  Please enter a value in the range of 8 - 64")
    return value
