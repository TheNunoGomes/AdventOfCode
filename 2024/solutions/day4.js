const {
  checkLetter,
  directionsToCheckP1,
  dirs,
} = require("../lib/day4-helpers");

function part1(data) {
  let xmasCount = 0;

  const lastCol = data[0].length - 1;
  const lastRow = data.length - 1;

  for (let y = 0; y < data.length; y++) {
    const lineCharacters = data[y];
    for (let x = 0; x < lineCharacters.length; x++) {
      const currentChar = lineCharacters[x];

      if (currentChar === "X") {
        const dirsToCheck = directionsToCheckP1(lastCol, lastRow, [x, y]);

        dirsToCheck.forEach(async (d) => {
          let nextCoords = [x + dirs[d][0], y + dirs[d][1]];

          const mCoords = checkLetter(data, nextCoords, "M");
          if (mCoords) {
            const [mX, mY] = mCoords;
            nextCoords = [mX + dirs[d][0], mY + dirs[d][1]];

            const aCoords = checkLetter(data, nextCoords, "A");
            if (aCoords) {
              const [aX, aY] = aCoords;
              nextCoords = [aX + dirs[d][0], aY + dirs[d][1]];

              const sCoords = checkLetter(data, nextCoords, "S");
              if (sCoords) {
                xmasCount++;
              }
            }
          }
        });
      }
    }
  }
  return xmasCount;
}

function part2(data) {
  let xmasCount = 0;

  // No need to check first and last rows
  for (let y = 1; y < data.length - 1; y++) {
    const lineCharacters = data[y];
    // No need to check first and last cols
    for (let x = 1; x < lineCharacters.length - 1; x++) {
      const currentChar = lineCharacters[x];
      if (currentChar === "A") {
        const ulCoords = [x + dirs["upLeft"][0], y + dirs["upLeft"][1]];
        const urCoords = [x + dirs["upRight"][0], y + dirs["upRight"][1]];
        const dlCoords = [x + dirs["downLeft"][0], y + dirs["downLeft"][1]];
        const drCoords = [x + dirs["downRight"][0], y + dirs["downRight"][1]];

        const upLeftCharIsM = checkLetter(data, ulCoords, "M");
        const downRightCharIsS = checkLetter(data, drCoords, "S");

        const firstMASOption1 = upLeftCharIsM && downRightCharIsS;

        const downRightIsM = checkLetter(data, drCoords, "M");
        const upLeftCharIsS = checkLetter(data, ulCoords, "S");

        const firstMASOption2 = downRightIsM && upLeftCharIsS;

        if (!firstMASOption1 && !firstMASOption2) {
          continue;
        }

        const upRightCharIsM = checkLetter(data, urCoords, "M");
        const downLeftCharIsS = checkLetter(data, dlCoords, "S");

        const secondMASOption1 = upRightCharIsM && downLeftCharIsS;

        const downLeftIsM = checkLetter(data, dlCoords, "M");
        const upRightCharIsS = checkLetter(data, urCoords, "S");

        const secondMASOption2 = downLeftIsM && upRightCharIsS;

        if (!secondMASOption1 && !secondMASOption2) {
          continue;
        }

        xmasCount++;
      }
    }
  }
  return xmasCount;
}

module.exports = {
  part1,
  part2,
};
