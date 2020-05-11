#!/usr/bin/node
const squareV1 = require('./5-square');

module.exports = class Square extends squareV1 {
  charPrint (c) {
    let cnt = 0;
    let print = '';
    if (c === 'C') {
      for (cnt = 0; cnt < this.width; cnt++) {
        print += c;
      }
      for (cnt = 0; cnt < this.height; cnt++) {
        console.log(print);
      }
    } else {
      super.print();
    }
  }
};
