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

  rotate () {
    const tmpWidth = this.width;
    const tmpHeight = this.height;
    this.width = tmpHeight;
    this.height = tmpWidth;
  }

  double () {
    const doubleWidth = this.width * 2;
    const doubleHeight = this.height * 2;
    this.width = doubleWidth;
    this.height = doubleHeight;
  }
};
