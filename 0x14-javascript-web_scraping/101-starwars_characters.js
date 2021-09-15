#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

function getfromApi (url) {
  return new Promise((resolve, reject) => {
    request(url, function (err, res, body) {
      if (err) reject(err);
      const name = JSON.parse(body);
      resolve(name);
    });
  });
}

async function getChars () {
  const data = await getfromApi('https://swapi-api.hbtn.io/api/films/' + argv[2]);
  const chars = data.characters;
  for (const element of chars) {
    const dataName = await getfromApi(element);
    const name = dataName.name;
    console.log(name);
  }
}

getChars();
