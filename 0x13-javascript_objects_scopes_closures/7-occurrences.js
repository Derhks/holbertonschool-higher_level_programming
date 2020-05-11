#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let cnt = 0;
  for (let itr = 0; itr < list.length; itr++) {
    if (list[itr] === searchElement) {
      cnt += 1;
    }
  }
  return cnt;
};
