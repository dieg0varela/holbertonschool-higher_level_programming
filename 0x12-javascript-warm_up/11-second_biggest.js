#!/usr/bin/node
const { argv } = require('process');

if (isNaN(argv[2]) || argv[2] === 1) {
  console.log('0');
}

let arr = argv.slice(2);
let cosa = arr.map(x => parseInt(x));
cosa.sort();
const len = cosa.length;
console.log(cosa[len - 2]);
