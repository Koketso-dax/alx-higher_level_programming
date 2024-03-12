#!/usr/bin/node

/**
 * Prints the number of arguments already printed and the new index value.
 * @param {*} item - The current argument value to print.
 */
exports.logMe = function (item) {
  // If the logMe.count property is undefined, set it to 0
  exports.logMe.count = exports.logMe.count || 0;

  // Print the output in the specified format
  console.log(`${exports.logMe.count}: ${item}`);

  // Increment the count for the next call
  exports.logMe.count++;
};
