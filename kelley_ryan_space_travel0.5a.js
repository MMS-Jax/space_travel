/*
Space Travel Calculator by Ryan K. 
Version 0.4a 
February 07, 2018
*/ 

// Declare important const variables first.  Distances measured in millions of kilometers. 

const distanceToMars = 1; // You need to enter the actual distance values here.  Do not use commas.  
const distanceToSun = 1; // Please note that variable names follow camelCase rules. 
const distanceToPluto = 1; 
const distanceToJupiter = 1; 
const distanceToNeptune = 1; 

// Distances for objects outside the Solar System. Also measured in millions of kilometers. 

const distanceToAlphaCentauri = 1;
const distanceToCrabNebula = 1;
const distanceToProximaCentauri = 1;
const distanceToEagleNebula = 1;
const distanceToPillarsOfCreation = 1; 

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


/* 
Next we need to have the user select a destination and save that data to a variable. 
Which of the following methods would work best?
    
    var user_choice = input("Type the number of the destination and press the [Enter] key.");
    var user_choice = read_data("Type the number of the destination and press the [Enter] key.");
    var user_choice = data_read("Type the number of the destination and press the [Enter] key.");
    var user_choice = prompt("Type the number of the destination and press the [Enter] key.");

Use your Internet research skills to determine which of the above lines of code would work best.     
*/ 

// REPLACE THIS LINE WITH THE CODE YOU WANT TO USE TO STORE THE USER'S CHOICE.

/*
Now that we have saved the user choice into a variable we need to figure out what to do with it.  There are at least two programming structures we can
use to accomplish this. 

One is using an if/else statement to determine which distance to use. 

    if (user_choice == 1) {
        console.log("You have chosen Mars.");
        var distance = distanceToMars;
    } else if (user_choice == 2) {
        console.log("You have chosen option 2.");
        var distance = distanceToOption2;
    } else {
        console.log("You did not choose a viable option.  The program will now close.");
    }

Another method is using a switch statement.  

    switch(user_choice) {
        case "1":
            console.log("You have chosen Mars.");
            var distance = distanceToMars;
            break;
        case "2":
            console.log("You have chosen option 2.");
            var distance = distanceToOption2;
            break
        default:
            console.log("You did not choose a viable option.  The program will now close.");
    }

Again, use your Internet research skills to determine which of the above you would like to use. 
*/ 

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
    }
*/ 