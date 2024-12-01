const { getMidnightEST } = require("./dates");

function hasValidArgumentsLength(argsLength) {
  if (![4, 5].includes(argsLength)) {
    throw new Error("Invalid number of arguments");
  }
}

function validateArguments(args) {
  let day, part;
  let test = false;

  for (let i = 0; i < args.length; ) {
    const flag = args[i];
    if (["-d", "--day"].includes(flag)) {
      day = Number(args[i + 1]);
      i += 2;
    } else if (["-p", "--part"].includes(flag)) {
      part = Number(args[i + 1]);
      i += 2;
    } else if (["-t", "--test"].includes(flag)) {
      test = true;
      i++;
    } else {
      throw new Error(`Invalid parameter: ${args[i]}`);
    }
  }
  return { day, part, test };
}

function validateDay(day) {
  if (!day) {
    throw new Error(`Please specify the day of the puzzle to solve`);
  }
  if (day < 1 || day > 25) {
    throw new Error(`Invalid day: ${day}`);
  }
  const now = new Date();
  const puzzleReleaseTime = getMidnightEST(now.getFullYear(), 12, day);
  if (now < puzzleReleaseTime) {
    throw new Error("This puzzle has not been released yet");
  }
}

function validatePart(part) {
  if (!part) {
    throw new Error(`Please specify the part of the puzzle to solve`);
  }
  if (![1, 2].includes(part)) {
    throw new Error(`Invalid part: ${part}`);
  }
}

function validate(args) {
  hasValidArgumentsLength(args.length);
  const argumentValues = validateArguments(args);
  validateDay(argumentValues.day);
  validatePart(argumentValues.part);

  return argumentValues;
}

module.exports = {
  validate,
  hasValidArgumentsLength,
  validateArguments,
  validateDay,
  validatePart,
};
