const { expect, test, describe } = require("@jest/globals");
const {
  hasValidArgumentsLength,
  validateArguments,
} = require("../lib/validations");

describe("Validations", () => {
  beforeAll(() => {
    // Mock Date to always return 2024-11-30T00:00:00.000Z
    const mockDate = new Date("2024-12-09T00:00:00.000Z");
    // jest.spyOn(global, "Date").mockImplementation(() => mockDate);
  });

  afterAll(() => {
    // Restore the original Date implementation
    // jest.restoreAllMocks();
  });

  describe("hasValidArgumentsLength", () => {
    test("should return with valid parameter - 4", () => {
      expect(hasValidArgumentsLength(4)).toStrictEqual();
    });

    test("should return with valid parameter - 5", () => {
      expect(hasValidArgumentsLength(5)).toStrictEqual();
    });

    test("should throw error with invalid parameter - 3", () => {
      expect(() => hasValidArgumentsLength(3)).toThrow(
        new Error("Invalid number of arguments")
      );
    });

    test("should throw error with invalid parameter - 6", () => {
      expect(() => hasValidArgumentsLength(6)).toThrow(
        new Error("Invalid number of arguments")
      );
    });
  });

  describe("validateArguments", () => {
    test("should return the day with short day flag", () => {
      const { day } = validateArguments(["-d", "21", "-p", "1"]);
      expect(day).toStrictEqual(21);
    });

    test("should return the part with short part flag", () => {
      const { part } = validateArguments(["-d", "21", "-p", "1"]);
      expect(part).toStrictEqual(1);
    });

    test("should return the test as true with short test flag", () => {
      const { test } = validateArguments(["-d", "21", "-p", "1", "-t"]);
      expect(test).toStrictEqual(true);
    });

    test("should return the day with long day flag", () => {
      const { day } = validateArguments(["--day", "21", "-p", "1"]);
      expect(day).toStrictEqual(21);
    });

    test("should return the part with short long flag", () => {
      const { part } = validateArguments(["-d", "21", "--part", "1"]);
      expect(part).toStrictEqual(1);
    });

    test("should return the test as true with long test flag", () => {
      const { test } = validateArguments(["-d", "21", "-p", "1", "--test"]);
      expect(test).toStrictEqual(true);
    });

    test("should return the test as false without", () => {
      const { test } = validateArguments(["-d", "21", "-p", "1"]);
      expect(test).toStrictEqual(false);
    });

    test("should return the right values in mixed order scenarios - scenario 1", () => {
      const { day, part, test } = validateArguments(["-p", "2", "-d", "12"]);
      expect(day).toStrictEqual(12);
      expect(part).toStrictEqual(2);
      expect(test).toStrictEqual(false);
    });

    test("should return the right values in mixed order scenarios - scenario 2", () => {
      const { day, part, test } = validateArguments([
        "--part",
        "2",
        "-t",
        "--day",
        "1",
      ]);
      expect(day).toStrictEqual(1);
      expect(part).toStrictEqual(2);
      expect(test).toStrictEqual(true);
    });

    test("should throw error for an invalid flag", () => {
      expect(() => validateArguments(["-part", "2", "--day", "1"])).toThrow(
        "Invalid parameter: -part"
      );
    });
  });
});
