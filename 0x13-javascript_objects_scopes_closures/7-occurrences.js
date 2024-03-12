#!/usr/bin/node
/**
 * Returns the number of occurrences of a specified element in a list.
 * @param {Array} list - The list to search for occurrences.
 * @param {*} searchElement - The element to count occurrences for.
 * @returns {number} - The number of occurrences of the specified element in the list.
 */
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, currentElement) => {
    return count + (currentElement === searchElement ? 1 : 0);
  }, 0);
};
