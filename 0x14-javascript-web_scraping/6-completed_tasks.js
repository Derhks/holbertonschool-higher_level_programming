#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error === null) {
    const listBody = JSON.parse(body);
    const dictTasks = {};
    let maxId = 0;
    for (let itr2 = 0; itr2 < listBody.length; itr2++) {
      maxId = listBody[itr2].userId;
    }
    for (let itr1 = 1; itr1 <= maxId; itr1++) {
      let cnt = 0;
      for (let itr2 = 0; itr2 < listBody.length; itr2++) {
        if (listBody[itr2].userId === itr1) {
          if (listBody[itr2].completed === true) {
            cnt++;
          }
        }
      }
      dictTasks[itr1] = cnt;
    }
    return console.log(dictTasks);
  } else {
    console.error(error);
  }
});
