#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const listBody = JSON.parse(body);
    const dictTasks = {};

    for (let itr = 0; itr < listBody.length; itr++) {
      if (listBody[itr].completed === true) {
        if (dictTasks[listBody[itr].userId] >= 1) {
          dictTasks[listBody[itr].userId] += 1;
        } else {
          dictTasks[listBody[itr].userId] = 1;
        }
      }
    }
    console.log(dictTasks);
  }
});
