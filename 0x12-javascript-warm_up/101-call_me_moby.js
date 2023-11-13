#!/usr/bin/node

function executeXTimes(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

function exampleFunction() {
  console.log("Executing exampleFunction");
}

executeXTimes(5, exampleFunction);
