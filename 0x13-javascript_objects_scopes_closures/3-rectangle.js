#!/usr/bin/node

/**
 * Represents a Rectangle.
 * @class
 */
class Rectangle {
  /**
     * Creates a new Rectangle with the specified width and height.
     * If w or h is equal to 0 or not a positive integer, creates an empty object.
     * @constructor
     * @param {number} w - The width of the rectangle.
     * @param {number} h - The height of the rectangle.
     */
  constructor (w, h) {
    /**
       * The width of the rectangle.
       * @member {number}
       */
    this.width = (typeof w === 'number' && w > 0) ? w : 0;

    /**
       * The height of the rectangle.
       * @member {number}
       */
    this.height = (typeof h === 'number' && h > 0) ? h : 0;

    if (this.width === 0 || this.height === 0) {
      // If width or height is 0, create an empty object
      return {};
    }
  }

  /**
     * Prints the rectangle using the character X.
     * @method
     */
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
