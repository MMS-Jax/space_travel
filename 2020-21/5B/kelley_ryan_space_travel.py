# Space Travel Simulator 2020, Ryan Kelley, 10/05/2020 9:09AM, Version 0.7
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
dist_pluto = 7.5 * billion 
dist_neptune = 4.3514 * billion



# Objects outside the Solar System
light_year = 9.46073 * trillion
dist_alpha_centauri = 4.3 * light_year
dist_eagle_nebula = 5700 * light_year
dist_pillars_creation = 7000 * light_year

print("/*********************************************************************************\\")
print("|  Please choose an object from the following menu.                               |")
print("|                                                                                 |")
print("|  [0] The Sun                                                                    |")
print("|  [1] Pluto                                                                      |")
print("|  [2] Neptune                                                                    |")
print("|  [3] Alpha Centauri                                                             |")
print("|  [4] Eagle Nebula                                                               |")
print("|  [5] Pillars of Creation                                                        |")
print("|                                                                                 |")
print("\\*********************************************************************************/")
time.sleep(3)
user_choice = int(input("Please type a number from the menu and press ENTER."))
# print(user_choice)
distance = 0

if user_choice == 0: # == means "Are these two things equal?"
    distance = dist_sun
    print("You have chosen The Sun. It is", distance, "kilometers from Earth.\n")
elif user_choice == 1: # == means "Are these two things equal?"
    distance = dist_pluto
    print("You have chosen Pluto. It is", distance, "kilometers from Earth.\n")
elif user_choice == 2: # == means "Are these two things equal?"
    distance = dist_neptune
    print("You have chosen Neptune. It is", distance, "kilometers from Earth.\n")
elif user_choice == 3: # == means "Are these two things equal?"
    distance = dist_alpha_centauri
    print("You have chosen Alpha Centauri. It is", distance, "kilometers from Earth.\n")
elif user_choice == 4: # == means "Are these two things equal?"
    distance = dist_eagle_nebula
    print("You have chosen the Eagle Nebula. It is", distance, "kilometers from Earth.\n")
elif user_choice == 5: # == means "Are these two things equal?"
    distance = dist_pillars_creation
    print("You have chosen Pillars of Creation. It is", distance, "kilometers from Earth.\n")
else:
    print("You did not choose an option on the menu.  Please restart the program.\n")
    exit() 
time.sleep(3)

light_speed = 299792
user_speed = int(input("Please type a speed in Km / s.  DO NOT enter commas.  Then press ENTER.\n"))
print(user_speed)

# Need to write if/elif/else statement to make sure user_speed <= light_speed.

VAVOPQ
