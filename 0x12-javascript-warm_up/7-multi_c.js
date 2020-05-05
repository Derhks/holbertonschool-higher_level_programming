#!/usr/bin/node
const times = parseInt(process.argv[2]);
let cnt = 0;
if (times) {
  for (cnt = 0; cnt < times; cnt++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
