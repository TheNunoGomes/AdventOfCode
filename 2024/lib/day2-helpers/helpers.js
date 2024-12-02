function hasTooManyDuplicateNumbers(report, threshold) {
  const reportSet = new Set(report);
  return reportSet.size < report.length - threshold;
}

function unsafeDiff(num1, num2) {
  return Math.abs(num1 - num2) > 3;
}

function unsafeOrder(num1, num2, ascending) {
  return (ascending && num1 > num2) || (!ascending && num1 < num2);
}

function isTooShortToBeUnsafe(length, threshold) {
  return length <= threshold;
}

module.exports = {
  hasTooManyDuplicateNumbers,
  unsafeDiff,
  unsafeOrder,
  isTooShortToBeUnsafe,
};
