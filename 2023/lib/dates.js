function getMidnightEST(year, month, day) {
  // Create a UTC date for the specified day
  const utcDate = new Date(Date.UTC(year, month - 1, day)); // month is 0-based

  // Adjust for EST (UTC-5)
  const estOffset = 5 * 60 * 60 * 1000; // 5 hours in milliseconds
  const estMidnight = new Date(utcDate.getTime() + estOffset);

  return estMidnight;
}

module.exports = { getMidnightEST };
