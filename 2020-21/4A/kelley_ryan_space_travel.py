# Space Travel Simulator, Ryan Kelley, 10/06/20, 2:22PM, Version 0.95
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
# print ("The distance to the Sun is", dist_sun, "kilometers.")
# print ("The distance to Pluto is", dist_pluto, "kilometers.")
# print ("The distance to Neptune is", dist_neptune, "kilometers.") 

# Distances to Objects Outside Our Solar System (Three) 
light_year = 9.469703 * trillion
dist_alpha_centauri = 4.3 * light_year
dist_eagle_nebula = 5700 * light_year
dist_pillars_creation = 7000 * light_year
# print ("The distance to Alpha Centauri is", dist_alpha_centauri, "kilometers.")
# print ("The distance to the Eagle Nebula is", dist_eagle_nebula, "kilometers.")
# print ("The distance to the Pillars of Creation is", dist_pillars_creation, "kilometers.") 

# Ask the User for their name.
user_name = input("Hello!  What is your name?  Please type it and press ENTER.\n")
print("Hello " ,user_name," I hope you are having a good day! Let's get started.\n")
time.sleep(3)


print ("[+---------------------------------------------------------------------+]")
print ("[ Please choose one of the options from the menu.                       ]")
print ("[                                                                       ]")
print ("[ [0] The Sun                                                           ]")
print ("[ [1] Pluto                                                             ]")
print ("[ [2] Neptune                                                           ]")
print ("[ [3] Alpha Centauri                                                    ]")
print ("[ [4] Eagle Nebula                                                      ]")
print ("[ [5] Pillars of Creation                                               ]")
print ("[                                                                       ]")
print ("[ You will be prompted to type the number for the object you want.      ]")
print ("[+---------------------------------------------------------------------+]")
time.sleep(2)


user_choice = int(input("Please type the number you want and press ENTER.\n"))
distance = 0
# print (user_choice)

if user_choice == 0:   # == means "Are these two equal?"
    distance = dist_sun
    print("You selected the Sun.  It is", distance," Km from the Earth.\n")
elif user_choice == 1:  
    distance = dist_pluto
    print("You selected Pluto.  It is", distance," Km from the Earth.\n")
elif user_choice == 2:  
    distance = dist_neptune
    print("You selected Neptune.  It is", distance," Km from the Earth.\n")
elif user_choice == 3:  
    distance = dist_alpha_centauri
    print("You selected Alpha Centauri.  It is", distance," Km from the Earth.\n")
elif user_choice == 4:  
    distance = dist_eagle_nebula
    print("You selected the Eagle Nebula.  It is", distance," Km from the Earth.\n")
elif user_choice == 5:  
    distance = dist_pillars_creation
    print("You selected the Pillars of Creation.  It is", distance," Km from the Earth.\n")
else: # This is the PANIK option.  It means none of my choices above were true.  
    print("You did not pick an option from the menu.  The program will now exit.  Try again.\n")
    exit() 


light_speed = 299792  # Km / s
user_speed = int(input("Please type a speed in Km / s.  Do NOT enter commas.\n"))
print("You entered",user_speed,"Km / s.  That's fast!\n")

if user_speed > light_speed:
    print("That's actually too fast, you can't break the laws of physics!\n")
    user_speed = int(input("Please type a speed in Km / s.  Do NOT enter commas.\n"))
    print("You entered",user_speed,"Km / s.  That's fast!\n")
else:
    print("You are not going faster than light speed.  Good luck!\n")
time.sleep(2)


trip_time = distance / user_speed  
print("It will take", trip_time,"seconds to complete the trip.\n") 


secs_per_year = 3.154e7
max_trip = secs_per_year * 3
time.sleep(2)

if trip_time > max_trip:
    print("The trip will take too long.  It is dangerous to go!\n")
else:
    print("The trip will be no more than three years.  Good luck, travel safely!\n")
time.sleep(2)




