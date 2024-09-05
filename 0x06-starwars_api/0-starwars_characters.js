#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, async (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  try {
    const charactersArray = JSON.parse(body).characters;
    for (const character of charactersArray) {
      await new Promise((resolve) => {
        request(character, (err, res, body) => {
          if (err) {
            console.error(err);
            resolve();
            return;
          }

          console.log(JSON.parse(body).name);
          resolve();
        });
      });
    }
  } catch (parseError) {
    console.error('Failed to parse response:', parseError);
  }
});
