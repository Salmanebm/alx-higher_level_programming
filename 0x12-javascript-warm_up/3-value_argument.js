#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log('Arguments:', process.argv.slice(2));
} 