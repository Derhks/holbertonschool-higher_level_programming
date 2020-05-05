#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
let sum = 0;
if (a && b) {
  sum = add(a, b);
  console.log(sum);
} else {
  console.log('NaN');
}
