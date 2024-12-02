const {
  hasTooManyDuplicateNumbers,
  isTooShortToBeUnsafe,
  unsafeDiff,
  unsafeOrder,
} = require("../lib/day2-helpers/helpers");

function isSafeReport(report) {
  if (
    hasTooManyDuplicateNumbers(report, 0) ||
    unsafeDiff(report[0], report[1])
  ) {
    return false;
  }

  if (isTooShortToBeUnsafe(report.length, 2)) {
    return true;
  }

  for (let j = 1; j < report.length - 1; j++) {
    const num1 = report[j];
    const num2 = report[j + 1];
    if (
      unsafeDiff(num1, num2) ||
      unsafeOrder(num1, num2, report[0] < report[1])
    ) {
      return false;
    }
  }

  return true;
}

function isSafeWithoutOneElement(report) {
  return report.some((_, i) =>
    isSafeReport([...report.slice(0, i), ...report.slice(i + 1)])
  );
}

function part1(data) {
  return data.filter((line) => {
    const report = line.split(" ").map(Number);
    return isSafeReport(report);
  }).length;
}

function part2(data) {
  return data.filter((line) => {
    const report = line.split(" ").map(Number);
    return isSafeReport(report) || isSafeWithoutOneElement(report);
  }).length;
}

module.exports = {
  part1,
  part2,
};
