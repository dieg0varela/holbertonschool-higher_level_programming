#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');

fs.readFile(argv[2], function (err, data) {
  if (err) throw err;
  fs.writeFile(argv[4], data, function (err) {
    if (err) {
      return console.error(err);
    }
  });
});

fs.readFile(argv[3], function (err, data) {
  if (err) throw err;
  fs.appendFile(argv[4], data, function (err) {
    if (err) throw err;
  });
});
