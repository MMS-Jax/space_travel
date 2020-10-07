# Space Travel Simulator, Ryan Kelley, 10/06/20 11:28PM, Version 1.0
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


# Ask the user what their name is.
user_name = input("Hello!  What is your name?  Please type your name and press ENTER.\n")
print("Wow! I have never met anyone named", user_name,"before.  It's nice to meet you!\n")
time.sleep(2)


print("%+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+%")
print("!                                Space Travel Simulator Menu                        !")
print("!                                                                                   !")
print("!  Please select an object from the menu.                                           !")
print("!                                                                                   !")
print("!  [0] The Sun                                                                      !")
print("!  [1] Venus                                                                        !")
print("!  [2] Europa                                                                       !")
print("!  [3] Alpha Centauri                                                               !")
print("!  [4] Eagle Nebula                                                                 !")
print("!  [5] Crab Nebula                                                                  !")
print("!                                                                                   !")
print("%+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+%")
time.sleep(2)


user_choice = int(input("Please type a number from the menu and press ENTER.\n"))
distance = 0


if user_choice == 0: # user_choice == 0 is a CONDITIONAL STATEMENT, is it true or false? == means, "IS the left side equal to the right side?"
    distance = dist_sun
    print(f"You have selected The Sun.  It is {distance:,} kilometers from the Earth.\n")
elif user_choice == 1: 
    distance = dist_venus
    print(f"You have selected Venus.  It is {distance:,} kilometers from the Earth.\n")
elif user_choice == 2: 
    distance = dist_europa
    print(f"You have selected Jupiter's moon: Europa.  It is {distance:,} kilometers from the Earth.\n")
elif user_choice == 3: 
    distance = dist_alpha_centauri
    print(f"You have selected the next closest star: Alpha Centauri.  It is {distance:,} kilometers from the Earth.\n")
elif user_choice == 4: 
    distance = dist_eagle_nebula
    print(f"You have selected the Eagle Nebula.  It is {distance:,} kilometers from the Earth.\n")
elif user_choice == 5: 
    distance = dist_crab_nebula
    print(f"You have selected the Crab Nebula.  It is {distance:,} kilometers from the Earth.\n")
else: # Nothing else has happened, what do I do?
    print("You did not choose an object from the menu.  The program will now exit.  Please restart and try again.\n")
    exit()
time.sleep(2)


light_speed = 299792 # This is speed of light in Km / s.
user_speed = int(input("Please enter a speed in Km / s. DO NOT use commas.\n"))
if user_speed > light_speed: # user_speed > light_speed is the CONDITIONAL.
    print("You CANNOT exceed light speed, which is 299,792 Km / s.  Please try again.\n")
    user_speed = int(input("Please enter a speed in Km / s. DO NOT use commas.\n"))
    print(f"You are going {user_speed:,} Km / s.\n")
else:
    print(f"You are going {user_speed:,} Km / s.\n")
    print("That's a good speed, you are not going faster than light speed!\n")
time.sleep(2)


trip_time = distance / user_speed # This will give you an answer in SECONDS. 
print(f"The trip will take {trip_time:,} seconds to complete!\n")
secs_per_year = 3.154e7
max_time = secs_per_year * 3
time.sleep(2)
                 

if trip_time <= max_time: # trip_time <= max_time is the CONDITIONAL.
    print("The trip will NOT exceed three years. The mission can succeed!\n")
else:
    print("The trip will take more than three years.  It is too dangerous to make that journey.\n")
time.sleep(2)


print("I hope you enjoyed the Space Travel Simulator.  Good luck in your journey!\n")
time.sleep(2)
exit()
