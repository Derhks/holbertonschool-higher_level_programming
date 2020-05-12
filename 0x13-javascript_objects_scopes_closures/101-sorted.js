#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
let maxValue = 0;
for (const key in dict) {
  if (dict[key] > maxValue) {
    maxValue = dict[key];
  }
}
for (let cnt = 1; cnt <= maxValue; cnt++) {
  const list = [];
  for (const key in dict) {
    if (dict[key] === cnt) {
      list.push(key);
      newDict[dict[key]] = list;
    }
  }
}
console.log(newDict);
