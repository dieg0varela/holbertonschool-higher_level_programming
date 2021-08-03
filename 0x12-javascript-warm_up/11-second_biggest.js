#!/usr/bin/node
const { argv } = require('process');

if (isNaN(argv[2]) || argv[2] === 1) {
  console.log('0');
}

const arr = argv.slice(2);
const cosa = arr.map(x => parseInt(x));
cosa.sort(function (a, b) { return a - b; });
const len = cosa.length;
console.log(cosa[len - 2]);
