#!/usr/bin/node

const SquareA = require('./5-square');

module.exports = class Square extends SquareA {
  charPrint (a) {
    if (a === undefined) {
      a = 'X';
    }
    process.stdout.write((a.repeat(this.width) + '\n').repeat(this.height));
  }
};
