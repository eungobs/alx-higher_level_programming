#!/usr/bin/node

function incrementAndCall(number, theFunction) {
  number++;
  theFunction(number);
}

// Example usage:
function exampleFunction(value) {
  console.log("Incremented value:", value);
}

incrementAndCall(5, exampleFunction);
