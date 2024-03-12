#!/usr/bin/node
const fs = require('fs');
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

fs.readFile(sourceFile1, 'utf8', (err1, data1) => {
  if (err1) {
    console.error(`Error reading ${sourceFile1}:`, err1);
    process.exit(1);
  }

  fs.readFile(sourceFile2, 'utf8', (err2, data2) => {
    if (err2) {
      console.error(`Error reading ${sourceFile2}:`, err2);
      process.exit(1);
    }

    const concatenatedData = String(data1 + data2 );

    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
        process.exit(1);
      }
    });
  });
});
