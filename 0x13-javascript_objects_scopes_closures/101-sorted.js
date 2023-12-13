#!/usr/bin/node
const { dict } = require('./101-data');

const newDict = {};

// Iterate over the keys in the original dictionary
Object.keys(dict).forEach((userId) => {
  const occurrences = dict[userId];

  // If occurrences is not a key in the new dictionary, create an empty array
  newDict[occurrences] = newDict[occurrences] || [];

  // Push the user id to the array corresponding to the occurrences
  newDict[occurrences].push(userId);
});

console.log('New Dictionary:', newDict);
