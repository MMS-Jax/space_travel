# Space Travel Simulator, Ryan Kelley, October 01, 2020 2:16PM, Version 0.65
import time

# ALGORITHM: step by step list of instructions to solve a problem / complete a task.
# print instructions for the user
# get user input for selection
# calculate distance to selection
# get user input for speed, check to make sure it does not exceed light speed
# calculate travel time

print ("Thank you for using the NASA Space Travel Simulator!  This program will determine whether you can safely travel in outer space.") 
# Line 9 is a STATEMENT.  A statement is a complete line of code.
# print is a METHOD.  A method is a "special ability" built in to Python that programmers can use.  


# DECLARING VARIABLES
# Variables allow us to store data.
# The main types of INTEGERS (int), DECIMALS (floats), and STRINGS (string).
# Variable names can be camelCase or snake_case.
# In Python, variable names can start with a letter or an underscore but NOT a number.
# game_1, num_eggs, amnt_gas, or _favorite_flavor are all LEGAL variable names in Python.


# INITIALIZING VARIABLES



# Create variables for million, billion, trillion. 
million = 1000000
billion = 1000000000
trillion = 1000000000000

# Objects in Outer Space
dist_sun = 150.01 * million
dist_uranus = 2.9 * billion
dist_asteroid_belt = 553.5 * million

# Objects Outside the Solar System
light_year = 9.4607 * trillion
dist_alpha_centauri = 4.0 * light_year
dist_ursa_major = 11.25 * light_year
dist_gw_orionis = 1000 * light_year

# Ask the user what their name is.
user_name = input("What is your name?  Please type your name and press [ENTER].\n")
print("Oh, you're finally awake!  It's nice to meet you" ,user_name, "!\n")
# time.sleep(3)

print("+========================================================================+")
print("* Please choose one of the objects from the menu.                        *")
print("*                                                                        *")
print("*   [0] The Sun                                                          *")
print("*   [1] Uranus                                                           *")
print("*   [2] Asteroid Belt                                                    *")
print("*   [3] Alpha Centauri                                                   *")
print("*   [4] Ursa Major                                                       *")
print("*   [5] GW Orionis                                                       *")
print("*                                                                        *")
print("*   You will be prompted to enter one of the numbers from the list.      *")
print("+========================================================================+")
# time.sleep(3)
user_choice = int(input("Please type a number from the menu and press ENTER.\n"))
# print(user_choice)

distance = 0

if user_choice == 0: # Called CONDITIONAL, == means "Are these equal?"
    distance = dist_sun
    print("You have chosen the Sun.  It is", distance,"kilometers from Earth.\n")
elif user_choice == 1: # Called CONDITIONAL, == means "Are these equal?"
    distance = dist_uranus
    print("You have chosen Uranus.  It is", distance,"kilometers from Earth.\n")
elif user_choice == 2: # Called CONDITIONAL, == means "Are these equal?"
    distance = dist_asteroid_belt
    print("You have chosen the Asteroid Belt.  It is", distance,"kilometers from Earth.\n")
elif user_choice == 3: # Called CONDITIONAL, == means "Are these equal?"
    distance = dist_alpha_centauri
    print("You have chosen Alpha Centauri.  It is", distance,"kilometers from Earth.\n")
elif user_choice == 4: # Called CONDITIONAL, == means "Are these equal?"
    distance = dist_ursa_major
    print("You have chosen Ursa Major.  It is", distance,"kilometers from Earth.\n")
elif user_choice == 5: # Called CONDITIONAL, == means "Are these equal?"
    distance = dist_gw_orionis
    print("You have chosen GW Orionis.  It is", distance,"kilometers from Earth.\n")
else: # Does NOT need a conditional.
    print("You did not choose an option from the menu.  Please restart!\n")
    exit() 
# time.sleep(3)

light_speed =  299792



user_speed = int(input("Please enter a speed in Km / s.  DO NOT enter commas. Type it and press enter."))
print(user_speed)     


