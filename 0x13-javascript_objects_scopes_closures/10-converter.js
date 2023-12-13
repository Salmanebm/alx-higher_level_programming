#!/usr/bin/node

exports.converter = function (base) {
  this.toString = function (num) {
    return num.toString(base);
  };
};
