#!/usr/bin/node
var cnt = 0;
exports.logMe = function (item) {
  console.log(cnt + ': ' + item);
  cnt += 1;
};
