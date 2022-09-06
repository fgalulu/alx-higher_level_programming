#!/usr/bin/node

const myVar = parseInt(process.argv[2]);
if (process.argv[2] === undefined || isNaN(myVar)) {
  console.log('My number: ' + myVar);
} else {
  console.log('Not a number');
}
