#!/usr/bin/node

const list = require('./100-data').list;

const res = list.map((element, index) => element * index);

console.log(list);
console.log(res);
