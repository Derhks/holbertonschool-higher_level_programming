#!/usr/bin/node
const msg = 'undefined';
if (process.argv[2] && process.argv[3]) {
  console.log(`${process.argv[2]} is ${process.argv[3]}`);
} else if (process.argv[2] && !process.argv[3]) {
  console.log(`${process.argv[2]} is ${msg}`);
} else {
  console.log(`${msg} is ${msg}`);
}
