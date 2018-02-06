/*
Space Travel Calculator by Ryan K. 
Version 0.2a 
February 06, 2018
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

// Use console.log() to provide a list of options to the user.  One example is provided for you. 

console.log("[1] Mars");
