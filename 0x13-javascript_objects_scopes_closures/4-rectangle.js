/**
 * Represents a Rectangle.
 * @class
 */
class Rectangle {
  /**
     * Creates a new Rectangle with the specified width and height.
     * @constructor
     * @param {number} w - The width of the rectangle.
     * @param {number} h - The height of the rectangle.
     */
  constructor(w, h) {
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
  }

  /**
     * Prints the rectangle using the character X.
     * @method
     */
  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  /**
     * Exchanges the width and height of the rectangle.
     * @method
     */
  rotate() {
    [this.width, this.height] = [this.height, this.width];
  }

  /**
     * Doubles the width and height of the rectangle.
     * @method
     */
  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
