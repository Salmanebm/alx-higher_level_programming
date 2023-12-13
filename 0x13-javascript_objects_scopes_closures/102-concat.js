#!/usr/bin/node

const fs = require('fs');
const path = require('path');

if (process.argv.length !== 5) {
  console.log('Usage: node script.js <source-file-1> <source-file-2> <destination-file>');
  process.exit(1);
}

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

// Read the contents of the first source file
const content1 = fs.readFileSync(sourceFile1, 'utf-8');

// Read the contents of the second source file
const content2 = fs.readFileSync(sourceFile2, 'utf-8');

// Concatenate the contents of the two files
const concatenatedContent = content1 + content2;

// Write the concatenated content to the destination file
fs.writeFileSync(destinationFile, concatenatedContent);

console.log(concatenatedContent);
