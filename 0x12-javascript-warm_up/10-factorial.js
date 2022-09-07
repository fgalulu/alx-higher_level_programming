#!/usr/bin/node

const myVar = parseInt(process.argv[2]);

function myFactorial (a) {
  if (a === 1) {
    return 1;
  } else {
    return (a * myFactorial(a - 1));
  }
}
if (isNaN(myVar)) {
  console.log('1');
} else {
  console.log(myFactorial(myVar));
}
