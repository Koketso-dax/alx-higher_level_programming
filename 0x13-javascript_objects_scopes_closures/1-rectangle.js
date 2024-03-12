#!/usr/bin/node
/**
 * Represents Base Class with width & heigh attr.
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
module.exports = Rectangle;