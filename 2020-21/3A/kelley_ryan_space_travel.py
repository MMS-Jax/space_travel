# Space Travel Simulator, Ryan Kelley, 10/06/20 10:57AM, Version 0.45
# ALGORITHM -- List of step-by-step instructions to solve a problem / complete a task. 

import time 
# Print out a greeting and instructions.
# Provide a menu of places in outer space to travel to.
# Allow the user to select a place.
# Calculate the distance to that place.
# Ask the user how fast they are going.
# Determine how MUCH TIME it will take to get there.
# Determine if that is more than three years.


print ("Welcome to the NASA Space Travel Simulator!  This program will help you travel in space.")
# print() is known as a METHOD.  It is a built-in "ability" for Python programmers to use.


# DECLARING VARIABLES
# “Variables store different types of data.”
# Most Common Data Types are: INTEGERS, FLOATS, STRINGS, and BOOLS.”
# “Integers are positive or negative whole numbers, including zero. Abbreviated as int.”
# “Floats (floating point) are positive or negative numbers that have a decimal. Abbreviated as float.”
# “Strings are lines of text including letters and characters. Abbreviated as str.”
# “Bools (Boolean) are True of False values. Abbreviated as bool.”

# NAMING VARIABLES
# “Variables should ALWAYS be descriptive. Should be able to identify what type of data is stored in the variable.”
# “Examples include: num_eggs, amnt_gas, high_score, or player_name.”
# “Variables in Python can start with _ or a letter but NOT a number.”
# “Variables can use camelCase style or snake_case style but use the SAME style in your code.”


# “DECLARING and INITIALIZING VARIABLES”.
# “Declaring a variable means to tell Python the name of the variable.”
# “Generally variables will be declared on the first column of a line.”
# “INITIALIZING a variable means to assign it a starting value using the = symbol.”
# “In Python, the = symbols means to assign the variable on the left side the value of the statement or expression on the right side.”
# “my_score = 5x + 12"
# “The line above DECLARES a variable called my_score and INITIALIZES it to the value 5x + 12”


million = 1000000
billion = 1000000000
trillion = 1000000000000


# Objects in Our Solar System
dist_sun = 150 * million
dist_venus = 149.5 * million 
dist_europa = 630 * million


# Objects Outside of the Solar System
# Most objects outside of the Solar System are so far away they are measured in LIGHT YEARS.
light_year = 9.46073 * trillion
dist_alpha_centauri = 4.37 * light_year
dist_eagle_nebula = 7000 * light_year
dist_crab_nebula = 6500 * light_year


