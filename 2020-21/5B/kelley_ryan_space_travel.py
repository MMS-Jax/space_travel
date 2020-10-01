# Space Travel Simulator 2020, Ryan Kelley, 10/01/2020 9:15AM, Version 0.5
import time 
# print instructions on the screen
# get user input to select an object
# determine distance to the object
# get user input for speed 
# make sure it's not faster than speed of light
# calculate travel time
# determine if travel time is greater than 3 years.
# if more than three years, PRINT WARNING OF GRAVE DANGER OR DEATH
# if less than or equal to three years, PRINT HAPPY MESSAGE OF GOOD LUCK
# ALGORITHM - a step-by-step process to solve a problem / complete a task.  


print ("Hello!  Thank you for using the NASA Space Travel Simulator 2020!  This program will help you travel through space.")
# Line 15 is a STATEMENT.  A statement is one complete line of code.  
# print is a METHOD.  Methods are basically "special abilities" built in to the Python code. 


# DECLARING VARIABLES
# Variables are designed to store different types of data, such as high score, number of eggs, amount of gas, etc.
# Two main ways of writing variable names:  camelCase or snake_case.
# Variable names SHOULD TELL YOU WHAT TYPE OF DATA THEY ARE STORING.
# For example: amnt_gas, num_eggs, high_score are all good variable names.
# a_g, n_e, or h_s are NOT good variable names.
# Variables in Python must start with an _ or a letter.  And they can contain numbers.
# For example: score1, eggs0, etc.

# DATA TYPES
# INTEGER, written as int, any postive/negative whole number, including zero.
# FLOAT, written as float, any postive/negative number that has a decimal.
# BOOLEAN, written as bool, either TRUE or FALSE.
# STRINGS, written as str, a "string" of characters/numbers.  


user_name = input("What is your name?  Please type it and then press [ENTER].\n")
# input() is a METHOD to accept data from the user via the keyboard.
# input() allows us to print a STRING on the screen, usually with instructions.
# \n is a NEWLINE character, it is the same as pushing the ENTER key.
print("You entered",user_name,".\n")
time.sleep(3)


# Millions, Billions, Trillions

million = 1000000
billion = 1000000000
trillion = 1000000000000


# Objects in Our Solar System
dist_sun = 149.75 * million
# dist_venus =
# dist_europa


# Objects outside the Solar System
light_year = 9.46073 * trillion
dist_alpha_centauri = 4.3 * light_year
# Distance for object two goes here.
# Distance for object three goes here.

print("/*********************************************************************************\\")
print("|  Please choose an object from the following menu.                               |")
print("|                                                                                 |")
print("|  [0] The Sun                                                                    |")
print("|  [1] Venus                                                                      |")
print("|  [2] Europa                                                                     |")
print("|  [3] Alpha Centauri                                                             |")
print("|  [4] Something Else                                                             |")
print("|  [5] Another Something Else                                                     |")
print("|                                                                                 |")
print("|                                                                                 |")
print("|                                                                                 |")
print("|                                                                                 |")
print("|                                                                                 |")
print("\\*********************************************************************************/")


