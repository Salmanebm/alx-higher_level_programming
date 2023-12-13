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

  print () {
    if (this.width === 0 || this.height === 0) {
      console.log('Empty Rectangle');
      return;
    }

    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
