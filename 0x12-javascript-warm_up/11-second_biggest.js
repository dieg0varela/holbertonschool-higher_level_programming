#!/usr/bin/node
const { argv } = require('process');

if (isNaN(argv[2]) || argv[2] === 1) {
  console.log('0');
}

const arr = argv.slice(2);
arr.sort();
const len = arr.length;
console.log(arr[len - 2]);
