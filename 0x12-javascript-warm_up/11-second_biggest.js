#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let cnt = 2;
  let list = [];
  for (cnt = 2; cnt < process.argv.length; cnt++) {
    list.push(parseInt(process.argv[cnt]));
  }
  list = list.sort(function (a, b) {
    return a - b;
  });
  console.log(list[list.length - 2]);
}
