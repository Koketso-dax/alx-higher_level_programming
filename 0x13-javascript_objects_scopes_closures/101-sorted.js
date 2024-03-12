#!/usr/bin/node

// Importing the dictionary from 101-data.js
const { dict } = require('./101-data');

// Computing a new dictionary of user ids by occurrence
const newUserDict = {};

// Iterating through the original dictionary
for (const userId in dict) {
  const occurrences = dict[userId];

  // If occurrences is not a key in the new dictionary, create an empty array
  newUserDict[occurrences] = newUserDict[occurrences] || [];

  // Push the current userId to the array for the corresponding occurrences
  newUserDict[occurrences].push(userId);
}

// Printing the new dictionary
console.log(newUserDict);
