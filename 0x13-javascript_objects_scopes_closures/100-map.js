#!/usr/bin/node
const list = require('./100-data').list;
let cnt = 0;
const newData = list.map(function (x) {
  const newValue = x * cnt;
  cnt += 1;
  return newValue;
});
console.log(list);
console.log(newData);
