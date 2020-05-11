#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let cnt = 0;
    let print = '';
    for (cnt = 0; cnt < this.width; cnt++) {
      print += 'X';
    }
    for (cnt = 0; cnt < this.height; cnt++) {
      console.log(print);
    }
  }
};
