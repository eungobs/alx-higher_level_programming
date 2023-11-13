#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const sortedArgs = args.sort((a, b) => b - a);
console.log(sortedArgs.length < 2 ? 0 : sortedArgs[1]);
