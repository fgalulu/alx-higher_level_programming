#!/usr/bin/node

let myVar = parseInt(process.argv[2]);

if (isNaN(myVar) || process.argv[2] === undefined) {
  console.log('Missing size');
}
let myString = 'X';
for (let i = 1; i < myVar; i++) {
  myString += 'X';
}
while (myVar > 0) {
  console.log(myString);
  myVar--;
}
