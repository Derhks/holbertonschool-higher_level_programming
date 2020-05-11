#!/usr/bin/node
exports.esrever = function (list) {
  const reverseList = [];
  for (let itr = list.length - 1; itr >= 0; itr--) {
    reverseList.push(list[itr]);
  }
  return reverseList;
};
