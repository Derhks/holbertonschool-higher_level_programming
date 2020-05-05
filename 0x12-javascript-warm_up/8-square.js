#!/usr/bin/node
const area = parseInt(process.argv[2]);
let cnt = 0;
let print = '';
if (area) {
  for (cnt = 0; cnt < area; cnt++) {
    print += 'X';
  }
  for (cnt = 0; cnt < area; cnt++) {
    console.log(print);
  }
} else {
  console.log('Missing size');
}
