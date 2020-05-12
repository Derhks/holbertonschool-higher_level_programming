#!/usr/bin/node
const fs = require('fs');
const f1 = process.argv[2];
const f2 = process.argv[3];
const f3 = process.argv[4];

fs.readFile(f1, 'utf-8', (err, data) => {
  if (err) {
    return console.error(err);
  } else {
    fs.writeFile(f3, data, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});

fs.readFile(f2, 'utf-8', (err, data) => {
  if (err) {
    return console.error(err);
  } else {
    fs.appendFile(f3, data, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
