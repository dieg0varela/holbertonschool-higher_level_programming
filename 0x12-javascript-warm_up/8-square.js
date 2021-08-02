#!/usr/bin/node
const { argv } = require('process');
const Size = parseInt(argv[2]);
if (Number.isNaN(Size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Size; i++) {
    console.log('X'.repeat(Size));
  }
}
