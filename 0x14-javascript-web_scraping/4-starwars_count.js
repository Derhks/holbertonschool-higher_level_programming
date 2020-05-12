#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let cnt = 0;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    for (let itr = 0; itr < JSON.parse(body).results.length; itr++) {
      const listPeople = JSON.parse(body).results[itr].characters;
      for (let itr2 = 0; itr2 < listPeople.length; itr2++) {
        if (listPeople[itr2].includes(18)) {
          cnt++;
        }
      }
    }
    console.log(cnt);
  }
});
