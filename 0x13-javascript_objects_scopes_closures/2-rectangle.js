#!/usr/bin/node
/**
 * Rectangle class with type validation.
 * @class
 */
class Rectangle {
  /**
     * init new Rectangle with given width and height.
     * @constructor
     * @param {number} w - input width of rect
     * @param {number} h - input height of rect
     */
  constructor (w, h) {
    if (this.isValidParameters(w, h)) {
      /**
         * rectangle width.
         * @member {number}
         */
      this.width = w;
      /**
         * rectangle height.
         * @member {number}
         */
      this.height = h;
    }
  }

  /**
   * checks if init values are valid.
   * @private
   * @param {number} w - width to be validated.
   * @param {number} h - height to be validated.
   * @returns {boolean} - true if valid, false otherwise.
   */
  isValidParameters (w, h) {
    return typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0;
  }
}
module.exports = Rectangle;
