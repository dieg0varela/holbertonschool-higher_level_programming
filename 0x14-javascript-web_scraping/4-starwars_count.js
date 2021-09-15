#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request(argv[2], function (err, res, body) {
  if (err) console.log(err);
  const data = JSON.parse(body);
  let pichu = 0;
  data.results.forEach(element => {
    if (element.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      pichu++;
    }
  });
  console.log(pichu);
});
