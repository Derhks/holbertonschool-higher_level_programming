#!/usr/bin/node
let total = 1;
function factorial (numb) {
  if (numb === 0) {
    return 1;
  }
  if (isNaN(numb)) {
    return 1;
  }
  if (/^[0-9]*?.[0-9]*$/.test(numb)) {
    total = total * numb;
    factorial(numb - 1);
    return total;
  }
}
const numb = process.argv[2];
console.log(factorial(numb));
