#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let pichu = 0;
  list.forEach(element => {
    if (element === searchElement) {
      pichu++;
    }
  });
  return (pichu);
};
