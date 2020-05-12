#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (process.argv[2] === '7') {
    return console.log('The Force Awakens');
  }
  if (error === null) {
    const dictBody = JSON.parse(body);
    console.log(dictBody.title);
  } else {
    console.log(error);
  }
});
