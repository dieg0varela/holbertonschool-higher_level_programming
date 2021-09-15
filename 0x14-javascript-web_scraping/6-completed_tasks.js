#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request(argv[2], function (err, res, body) {
  if (err) console.log(err);
  const data = JSON.parse(body);
  const pichu = {};
  let id = 1;
  let num = 0;
  data.forEach(element => {
    if (element.userId === id) {
      if (element.completed === true) {
        num++;
      }
    } else {
      pichu[id] = num;
      id = element.userId;
      num = 0;
      if (element.completed === true) {
        num++;
      }
    }
  });
  pichu[id] = num;
  console.log(pichu);
});
