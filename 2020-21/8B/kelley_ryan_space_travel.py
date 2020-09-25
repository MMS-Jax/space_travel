# Space Travel Simulator, Ryan Kelley, September 25, 2020 2:16PM, Version 0.4

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

# light_speed = 299792
# DECLARED light_speed as a variable.  The = sign INITIALIZES the variable, which means giving it a starting value.
# print("The speed of light is", light_speed, "Km / s.") 
# When you use a variable_name inside of a string it is called SUBSTITUTION. 

# user_selection = input("Please enter a number and then press enter. ")
# The = translates to the English phrase "MAKE EQUAL TO" or "SET EQUAL TO. 
# print(user_selection)

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
print(user_name)



