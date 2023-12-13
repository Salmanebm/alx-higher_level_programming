#!/usr/bin/node
const SquareB = require('./5-square.js');

class Square extends SquareB {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    c = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
