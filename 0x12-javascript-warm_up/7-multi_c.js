#!/usr/bin/node
const argv = require('process').argv;
const times = parseInt(argv[2]);
const message = 'C is fun';

if (times) {
  for (let i = 0; i < times; i++) {
    console.log(message);
  }
} else {
  console.log('Missing number of occurrences');
}
