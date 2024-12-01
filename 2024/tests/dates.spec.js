const { expect, test, describe } = require("@jest/globals");
const { getMidnightEST } = require("../lib/dates");

describe("Dates", () => {
  describe("getMidnightEST", () => {
    test("should return the correct time", () => {
      const year = 2024;
      const month = 12;
      const day = 21;

      const expectedDate = new Date(year, month - 1, day, 5); // Has to be month - 1 because months start at 0
      expect(getMidnightEST(year, month, day)).toStrictEqual(expectedDate);
    });
  });
});
