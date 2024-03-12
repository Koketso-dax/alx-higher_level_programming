#!/usr/bin/node
const BaseSquare = require('./5-square');
/**
 * Represents a Square, inheriting from Square.
 * @class
 * @extends BaseSquare
 */
class Square extends BaseSquare {
  /**
     * Prints the square using the specified character c.
     * If c is undefined, uses X character.
     * @method
     * @param {string} [c] - The character to print the square.
     */
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
