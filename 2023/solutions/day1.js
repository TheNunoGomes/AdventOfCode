function part1(data) {
  const numbers = data.map((line) => {
    const digits = line.replace(/[^0-9]/g, "");

    if (digits.length === 0) {
      return 0;
    }
    if (digits.length === 1) {
      return Number(`${digits[0]}${digits[0]}`);
    }
    return Number(`${digits[0]}${digits[digits.length - 1]}`);
  });
  return numbers.reduce((sum, n) => (sum += n));
}

function part2(data) {}

module.exports = {
  part1,
  part2,
};
