#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error === null) {
    const dictBody = JSON.parse(body);
    console.log(dictBody.title);
  } else {
    console.log(error);
  }
});
