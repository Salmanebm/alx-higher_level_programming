#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (this.isValidDimension(w) && this.isValidDimension(h)) {
      this.width = w;
      this.height = h;
    }
  }

  isValidDimension (dimension) {
    return typeof dimension === 'number' && dimension > 0 && Number.isInteger(dimension);
  }
}
module.exports = Rectangle;
