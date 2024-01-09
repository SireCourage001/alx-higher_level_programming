#!/usr/bin/node
const Square = require('./5-square');

module.exports = class Square extends Square {
charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let m = 0; m < this.height; m++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
};
