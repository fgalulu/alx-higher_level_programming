#!/usr/bin/node

const firstNumber = parseInt(process.argv[2]);
const secondNumber = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(firstNumber, secondNumber));
