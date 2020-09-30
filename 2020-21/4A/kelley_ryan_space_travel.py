# Space Travel Simulator, Ryan Kelley, Sept. 30, 2020, 2:32PM, Version 0.5
# ALGORITHM -- Step by step list of instructions to complete a task.
import time 
# print instructions
# get user selection
# calculate the distance to the object
# ask how fast you are traveling
# calculate how long it will take (Distance / Speed)
# Check to see if the trip takes more or less than three years.
# If the trip is MORE THAN 3 years, print a warning
# If the trip is LESS THAN OR EQUAL TO 3 years, print a message of success.


print ("Thank you for using the NASA Space Travel Simulator!")
# print is a METHOD used in Python.  methods are "special abilities" you can use. 


# DECLARING VARIABLES
# variables store DATA.
# Examples of Data include: INTEGERS, FLOATS (decimals), and STRINGS (text).
# Integers are WHOLE NUMBERS, POSITIVE OR NEGATIVE, including ZERO
# Floats are any POSITIVE or NEGATIVE NUMBER WITH A DECIMAL
# STRINGS are written text. 
# Naming Variables
# camelCase
# snake_case
# Variables in Python can start with _ or a letter, and can contain numbers.
# Variables should BE DESCRIPTIVE.

# Distances to Objects in Our Solar System (Three)
million = 1000000
billion = 1000000000
trillion = 1000000000000

dist_sun = 149.59787 * million 
dist_pluto = 7.5 * billion 
dist_neptune = 4.3514 * billion
print ("The distance to the Sun is", dist_sun, "kilometers.")
print ("The distance to Pluto is", dist_pluto, "kilometers.")
print ("The distance to Neptune is", dist_neptune, "kilometers.") 

# Distances to Objects Outside Our Solar System (Three) 
light_year = 9.469703 * trillion
dist_alpha_centauri = 4.3 * light_year
dist_eagle_nebula = 5700 * light_year
dist_pillars_creation = 7000 * light_year
print ("The distance to Alpha Centauri is", dist_alpha_centauri, "kilometers.")
print ("The distance to the Eagle Nebula is", dist_eagle_nebula, "kilometers.")
print ("The distance to the Pillars of Creation is", dist_pillars_creation, "kilometers.") 

# Ask the User for their name.
user_name = input("Hello!  What is your name?  Please type it and press ENTER.\n")
print("Hello " ,user_name," I hope you are having a good day! Let's get started.\n")
time.sleep(3)
