#!/usr/bin/node
const args = process.argv.slice(2).map(Number).sort((a, b) => a - b);
console.log(args.length <= 1 ? 0 : args[args.length - 2]);