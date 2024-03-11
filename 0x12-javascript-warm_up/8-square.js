#!/usr/bin/node
const size = process.argv[2];
if (isNaN(size) || size === undefined) {
    console.log("Missing size");
} else {
    const sizeInt = parseInt(size);

    for (let i = 0; i < sizeInt; i++) {
        let row = '';
        for (let j = 0; j < sizeInt; j++) {
            row += 'x';
        }
        console.log(row);
    }
}