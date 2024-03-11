#!/usr/bin/node
const size = process.argv[2];
function printSquare (size) {
  if (!parseInt(size)) {
    console.log('Missing size');
    return;
  }

  for (let i = 0; i < size; i++) {
    const row = 'X'.repeat(size);
    console.log(row);
  }
}

printSquare(size);
