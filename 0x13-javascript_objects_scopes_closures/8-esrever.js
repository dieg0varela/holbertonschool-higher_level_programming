#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  const ret = [];
  for (let i = len - 1; i >= 0; i--) {
    ret.push(list[i]);
  }
  return (ret);
};
