# Space Travel Simulator, Ryan Kelley, October 01, 2020 1:42PM, Version 0.5
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
# dist_alpha_centauri = 
# dist_ursa_major =
light_year = 9.4607 * trillion 
dist_gw_orionis = 1000 * light_year

# Ask the user what their name is.
user_name = input("What is your name?  Please type your name and press [ENTER].\n")
print("Oh, you're finally awake!  It's nice to meet you" ,user_name, "!\n")
time.sleep(3)




