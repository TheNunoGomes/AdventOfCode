const { readFile, parseContent } = require("./files");

function importSolution(solutionFile, solutionFunction) {
  try {
    const solution = require(`../solutions/${solutionFile}`)[solutionFunction];
    // If solution is undefined, it means the solution file exists, but the solution function does not
    if (!solution) {
      throw ""; // Doesn't matter what I'm throwing, cause I'm not catching it
    }
    return solution;
  } catch {
    throw new Error("This solution is not available yet");
  }
}

function solve(day, part, test) {
  const solutionFile = `day${day}`;
  const inputFile = `./datasets/day${day}${test ? "_t" : ""}.txt`;
  const solutionFunction = `part${part}`;
  const solution = importSolution(solutionFile, solutionFunction);
  const input = readFile(inputFile);
  const data = parseContent(input);
  console.log(`Solving day ${day} part ${part} ${test ? "test" : "challenge"}`);
  return solution(data);
}

module.exports = { solve };
