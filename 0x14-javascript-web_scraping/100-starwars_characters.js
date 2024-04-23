#!/usr/bin/node
const request = require('request');

// Check if movie ID is provided
if (process.argv.length < 3) {
    console.error('Please provide the movie ID as an argument.');
    process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to the Star Wars API to get movie details
request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
    } else if (response.statusCode !== 200) {
        console.error('Unexpected status code:', response.statusCode);
    } else {
        const movie = JSON.parse(body);
        console.log(`Characters of ${movie.title}:`);
        movie.characters.forEach(characterUrl => {
            // Fetch each character's details
            request(characterUrl, (charError, charResponse, charBody) => {
                if (charError) {
                    console.error('Error:', charError);
                } else if (charResponse.statusCode !== 200) {
                    console.error('Unexpected status code:', charResponse.statusCode);
                } else {
                    const character = JSON.parse(charBody);
                    console.log(character.name);
                }
            });
        });
    }
});
