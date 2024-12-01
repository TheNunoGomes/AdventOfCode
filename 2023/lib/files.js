const fs = require("fs");

function readFile(path) {
  const inputBuffer = fs.readFileSync(path);
  const input = String.fromCharCode(...new Uint8Array(inputBuffer));
  return input;
}

function parseContent(content) {
  return content.replace(/\r/g, "").split("\n");
}

module.exports = { readFile, parseContent };
