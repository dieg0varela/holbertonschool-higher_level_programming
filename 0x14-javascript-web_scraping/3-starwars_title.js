#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + argv[2], function (err, res, body) {
  if (err) console.log(err);
  const data = JSON.parse(body);
  console.log(data.title);
});
