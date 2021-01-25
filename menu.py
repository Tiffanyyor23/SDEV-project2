"""
   The purpose of this program is to provide the user with a menu of options
   math related options to perform.

"""

import sys
from datetime import date
from math import cos, sqrt, radians, pi
import password_generator
from verification import check_if_value_is_alpha, check_if_value_is_numeric


menu_options = {"a": "Generate Password", "b": "Calculate and Format A Percentage",
                "c": "How Many Days From Today Until July 4, 2025",
                "d": "Use the Law of Cosines to Calculate the Leg of A Triangle",
                "e": "Calculate the Volume of A Right Circular Cylinder",
                "f": "Exit Program"}


def calculate_percentage(num, demon, point):
    # This function calculates a percentage.
    percentage = round(num/demon, point)
    print(f' Based on your input, the percentage is {percentage}')


def days_until_july_4_2025():
    # This function returns the number of days left until July 4, 2025.
    current = date.today()
    july_4th = date(2025, 7, 4)
    print(f' There are {current - july_4th} days until July 4, 2025')


def calculate_leg_of_triangle(a, b, degree):
    # This function prints the leg leg of a triangle.
    value = round(sqrt((a ** 2 + b ** 2) - ((2 * a * b) * cos(radians(degree)))), 2)
    print(f'Based on your input, the answer is {value}.')


def calculate_volume_of_right_cylinder(r, h):
    # This function returns the volume of a right cylinder.
    volume = round(pi * (r ** 2) * h, 2)
    print(f'Based on your input, the volume of a right cylinder is {volume} ')


print("Welcome to the Math and Security Program.  \nBelow are the available options. "
      " \nPlease select the letter associated with the selection you would like to choose.\n \n")
for choice, option in menu_options.items():
    print(f'{choice} : {option}')

selection = input("\nSelection: ").lower()
check_if_value_is_alpha(selection, 1)
if selection == "a":
    password_generator.main()
elif selection == "b":
    numerator = check_if_value_is_numeric(input("Please enter the numerator: "))
    denominator = check_if_value_is_numeric(input("Please enter the denominator: "))
    decimal_point = check_if_value_is_numeric(input("Please enter how many decimal places to round to: "))
    calculate_percentage(numerator, denominator, decimal_point)
elif selection == "c":
    days_until_july_4_2025()
elif selection == "d":
    a_leg = check_if_value_is_numeric(input("Please enter the value for the leg a: "))
    b_leg = check_if_value_is_numeric(input("Please enter the value for the leg b: "))
    C = check_if_value_is_numeric(input("Please enter the value for angle C: "))
    calculate_leg_of_triangle(a_leg, b_leg, C)
elif selection == "e":
    radius = check_if_value_is_numeric(input("Please enter the radius of the cylinder: "))
    height = check_if_value_is_numeric(input("Please enter the height of the cylinder: "))
    calculate_volume_of_right_cylinder(radius, height)
elif selection == "f":
    check_if_value_is_alpha(selection, 1)
    print("Thank you for coming. \nExiting Program.")
    sys.exit()
else:
    print("The value you entered is not a valid option. Please only enter a "
          "value that corresponds to the options printed on the screen: ")
