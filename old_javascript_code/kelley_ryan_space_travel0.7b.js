/*
Space Travel Calculator by Ryan K. 
Version 0.6a 
February 09, 2018
*/ 

// Declare million and billion as variables. 
const million = 1000000;
const billion = 1000000000;
const trillion = 1000000000000;

/*
Distances measured in kilometers. 
Please note that variable names follow camelCase rules. 
*/ 

const distanceToMars = 54.6 * million;  
const distanceToSun = 92.96 * million; 
const distanceToJupiter = 588 * million; 
const distanceToPluto = 7.5 * billion; 
const distanceToNeptune = 2.7 * billion; 
const distanceToAlphaCentauri = 41.32 * trillion;
const distanceToProximaCentauri = 40.14 * trillion;
const distanceToCrabNebula = 6.171e16;
const distanceToEagleNebula = 6.622e16;
const distanceToPillarsOfCreation = 6.6225e16; 

// Let's explain what the program does to the user.  You need to change this to your own words.  
console.log("Welcome to the Space Travel Calculator!");
console.log("NASA has researched a number of objects inside and outside of the Solar System.");
console.log("This program will help calculate the amount of travel time to each of the objects.");
console.log("You will need to select one of the objects from the list."); 


// Use console.log() to provide a list of options to the user.  The user will select their destination by typing in the number from the list.   
console.log("[0] Mars");
console.log("[1] Sun");
console.log("[2] Jupiter");
console.log("[3] Pluto");
console.log("[4] Neptune");
console.log("[5] Alpha Centauri");
console.log("[6] Proxima Centauri");
console.log("[7] The Crab Nebula");
console.log("[8] Eagle Nebula");
console.log("[9] The Pillars of Creation");

// Ask the user where they want to go. Save that value as a variable named user_choice.
var user_choice = prompt("Type the number of the destination from the list and press the [Enter] key.");

// Next we need to determine which desination was chosen. 
if (user_choice == 0) {
    console.log("You have chosen Mars.");
    var distance = distanceToMars;
} else if (user_choice == 1) {
    console.log("You have chosen The Sun");
    var distance = distanceToSun;
} else if (user_choice == 2) {
    console.log("You have chosen Jupiter.");
    var distance = distanceToJupiter;
} else if (user_choice == 3) {
    console.log("You have chosen Pluto");
    var distance = distanceToPluto;
} else if (user_choice == 4) {
    console.log("You have chosen Neptune.");
    var distance = distanceToNeptune;
} else if (user_choice == 5) {
    console.log("You have chosen Alpha Centauri.");
    var distance = distanceToAlphaCentauri;
} else if (user_choice == 6) {
    console.log("You have chosen Proxima Centauri");
    var distance = distanceToProximaCentauri;
} else if (user_choice == 7) {
    console.log("You have chosen The Crab Nebula");
    var distance = distanceToCrabNebula;
} else if (user_choice == 8) {
    console.log("You have chosen The Eagle Nebula.");
    var distance = distanceToEagleNebula;
} else if (user_choice == 9) {
    console.log("You have chosen The Pillars of Creation.");
    var distance = distanceToPillarsOfCreation;
} else {
    console.log("You did not choose a viable option.  The program will not work correctly.");
}

// How fast do you want to go?  Measured in Km/s.  Replace YOUR_VARIABLE_HERE with a new name. 
var YOUR_VARIABLE_HERE = prompt("Please enter your speed in Km / s.  Do not exceed 300,000 Km / s. That is is the speed of light.");

// Make sure we are not violating the fundamental laws of physics. 
if (YOUR_VARIABLE_HERE > 300000) { // Replace YOUR_VARIABLE_HERE with the name used on line 86.
    var YOUR_VARIABLE_HERE = prompt("Enter your speed measured in Km/s.  Do not exceed the speed of light, 300,000 Km / s.");        
} else {
    console.log("You entered " + YOUR_VARIABLE_HERE + " Km / s."); // Replace YOUR_VARIABLE_HERE. 
}

// Calculate the travel time.  This answer is measured in seconds.   
var travelTime = YOUR_DISTANCE / YOUR_SPEED;

// The maximum travel time is three years.  How many seconds are in three years? Hint: it's not 0. 
const maxTravelTime = 0; 

// Determine if the mission can succeed or not. 
if (travelTime > maxTravelTime) { 
    console.log("At the chosen speed, the mission will exceed the three year limit.  The mission cannot succeed.");
} else {
    console.log("At the chosen speed, the travel time is no more than three years.  The mission can succeed.");
}