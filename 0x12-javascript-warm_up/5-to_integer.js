#!/usr/bin/node
const { argv } = require('process');
const Num = parseInt(argv[2]);
if (Number.isNaN(Num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Num);
}
