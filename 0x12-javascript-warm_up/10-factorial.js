#!/usr/bin/node
let total = 1;
function factorial (numb) {
  if (numb === 0) {
    return 1;
  } else if (isNaN(numb)) {
    return 1;
  } else {
    total = total * numb;
    factorial(numb - 1);
    return total;
  }
}
const numb = parseInt(process.argv[2]);
console.log(factorial(numb));
