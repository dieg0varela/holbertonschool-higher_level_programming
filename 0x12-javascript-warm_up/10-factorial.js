#!/usr/bin/node
const { argv } = require('process');

function fun (num) {
  const number = parseInt(num);
  if (isNaN(number) || number === 0) {
    return (1);
  }
  return (number * fun(number - 1));
}

console.log(fun(argv[2]));
