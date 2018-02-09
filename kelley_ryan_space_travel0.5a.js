/*
Space Travel Calculator by Ryan K. 
Version 0.5a 
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

/*
 Use console.log() to provide a list of options to the user.  One example is provided for you.  The user will select their destination by typing in 
 the number from the list.   
*/  
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
    console.log("You did not choose a viable option.  Please try again.");
}

/*  
Now that you have determined the destination, we need to figure out how fast you will travel. 
Write the code below this comment to have the user enter a speed in Km / s. 
*/ 

// WRITE THE CODE HERE TO ASK FOR THE SPEED OF TRAVEL. 

/* 
We need to make sure that our speed is not faster than the speed of light.  Light speed is 300,000 Km / s. 
Use an if statement to make sure that the speed entered is GREATER THAN 300,000.  If it is, make the user type a new speed. 

    if (SPEED > 300000) {
        // RE-USE THE CODE TO ENTER SPEED HERE.  
    } else {
        // Print the speed to the console so the user can confirm it is correct. 
    }
*/ 