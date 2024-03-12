#!/usr/bin/node

/**
 * Returns a function that converts a number from base 10 to another base.
 * @param {number} base - The base to which the number should be converted.
 * @returns {function} - The conversion function.
 */
exports.converter = function (base) {
  /**
     * Converts a number from base 10 to the specified base.
     * @param {number} num - The number to convert.
     */
  return function (num) {
    return Number(num).toString(base);
  };
};
