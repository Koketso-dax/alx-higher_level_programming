#!/usr/bin/node
/**
 * Returns the reversed version of a list.
 * @param {Array} list - The list to reverse.
 * @returns {Array} - The reversed version of the input list.
 */
exports.esrever = function (list) {
  // Create a new array to store the reversed elements
  const reversedList = [];

  // Iterate through the original list in reverse order and append elements to the new array
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  return reversedList;
};
