#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const wedgeAntilles = 'https://swapi-api.hbtn.io/api/people/18/';
let cnt = 0;

request(url, (error, response, body) => {
  if (error === null) {
    for (let itr = 0; itr < JSON.parse(body).results.length; itr++) {
      const listPeople = JSON.parse(body).results[itr].characters;
      for (let itr2 = 0; itr2 < listPeople.length; itr2++) {
        if (listPeople[itr2] === wedgeAntilles) {
          cnt++;
        }
      }
    }
    console.log(cnt);
  } else {
    console.log(error);
  }
});
