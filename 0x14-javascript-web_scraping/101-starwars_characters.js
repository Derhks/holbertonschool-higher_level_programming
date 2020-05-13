#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const dictMovie = JSON.parse(body);
    for (let cnt = 0; cnt < dictMovie.characters.length; cnt++) {
      const urlPeople = dictMovie.characters[cnt];
      request(urlPeople, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const dictPeople = JSON.parse(body);
          console.log(dictPeople.name);
        }
      });
    }
  }
});
