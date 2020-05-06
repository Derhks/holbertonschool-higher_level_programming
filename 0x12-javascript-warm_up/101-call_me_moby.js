#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  let cnt = 0;
  for (cnt = 0; cnt < x; cnt++) {
    theFunction();
  }
};
