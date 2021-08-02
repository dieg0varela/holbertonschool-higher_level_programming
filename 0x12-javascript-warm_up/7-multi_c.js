#!/usr/bin/node
const { argv } = require('process');
const Times = parseInt(argv[2]);
if (Number.isNaN(Times)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Times; i++) {
    console.log('C is fun');
  }
}
