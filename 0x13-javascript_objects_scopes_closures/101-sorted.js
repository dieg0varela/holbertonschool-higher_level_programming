#!/usr/bin/node

const dict = require('./101-data').dict;
const res = {};

for (const key in dict) {
  const value = dict[key];
  if (res[value] === undefined) {
    res[value] = [key];
  } else {
    res[value].push(key);
  }
}
console.log(res);
