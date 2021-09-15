#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request(argv[2], function (err, res, body) {
  if (err) console.log(err);
  const data = JSON.parse(body);
  let pichu = 0;
  data.results.forEach(element => {
    element.characters.forEach(char => {
      if (char.includes('18')) {
        pichu++;
      }
    });
  });
  console.log(pichu);
});
