#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request(argv[2], function (err, res, body) {
  if (err) console.log(err);
  const data = JSON.parse(body);
  const rai = {};
  data.forEach(element => {
    if (element.completed === true) {
      if (element.userId in rai) {
        rai[element.userId] += 1;
      } else {
        rai[element.userId] = 1;
      }
    }
  });
  console.log(rai);
});
