#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (searchElement in list) {
    count++;
  }
  return count;
};
