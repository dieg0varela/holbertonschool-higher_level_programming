#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');
const request = require('request');

request(argv[2], function(err, res, body) {
    console.log("code:",res.statusCode);
});
