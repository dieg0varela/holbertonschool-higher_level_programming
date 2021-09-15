#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');
const request = require('request');

request(argv[2], function (err, res, body) {
  if (err) console.log(err);
  try {
    fs.writeFileSync(argv[3], body, { encoding: 'utf8' });
  } catch (err) {
    console.error(err);
  }
});
