#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + argv[2], function (err, res, body) {
  if (err) console.log(err);
  const data = JSON.parse(body);
  data.characters.forEach(element => {
    request(element, function (err, res, body) {
      if (err) console.log(err);
      console.log(JSON.parse(body).name);
    });
  });
});
