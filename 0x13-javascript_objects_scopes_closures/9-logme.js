#!/usr/bin/node
const ArgsPrinted = [];
exports.logMe = function (item) {
  let count = 0;
  ArgsPrinted.forEach(Element => {
    count++;
  });
ArgsPrinted.push(item);
  console.log(count + ': ' + item);
};

