#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const path = process.argv[3];

request(url, (error, response, body) => {
  if (error === null) {
    fs.writeFile(path, body, err => {
      if (err) {
        console.error(err);
      }
    });
  } else {
    console.log(error);
  }
});
