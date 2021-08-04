#!/usr/bin/node

exports.converter = function (base) {
  return function calc (num) {
    return parseInt(num, 10).toString(base);
  };
};
