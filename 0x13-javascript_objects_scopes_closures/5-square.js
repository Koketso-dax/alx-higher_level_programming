#!/usr/bin/node

const Rectangle = require('./4-rectangle');
/**
 * Represents a Square, inheriting from Rectangle.
 * @class
 * @extends Rectangle
 */
class Square extends Rectangle {
    /**
     * Creates a new Square with the specified size.
     * @constructor
     * @param {number} size - The size of the square.
     */
    constructor(size) {
      // Calls the constructor of the parent class (Rectangle)
      super(size, size);
    }
  }
  module.exports = Square;