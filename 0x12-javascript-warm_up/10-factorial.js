#!/usr/bin/node
let total = 1;
function factorial (numb) {
  if (numb === 0) {
    return 1;
  }
  total = total * numb;
  factorial(numb - 1);
  return total;
}
const numb = parseInt(process.argv[2]);
let fact = 0;
if (numb) {
  fact = factorial(numb);
  console.log(fact);
} else {
  console.log(1);
}
