#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

try {
  const data = fs.readFileSync(argv[2], 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
