#!/usr/bin/node
const squareV1 = require('./5-square');

module.exports = class Square extends squareV1 {
  charPrint (c) {
    let print = '';
    if (c === undefined) {
      c = 'X';
    }
    for (let cnt = 0; cnt < this.width; cnt++) {
      print += c;
    }
    for (let cnt = 0; cnt < this.height; cnt++) {
      console.log(print);
    }
  }
};
