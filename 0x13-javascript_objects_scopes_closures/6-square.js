#!/usr/bin/node
const cuadrado = require('./5-square');

module.exports = class Square extends cuadrado {
  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
