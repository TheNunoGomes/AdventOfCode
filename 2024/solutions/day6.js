const { replaceCharacter } = require("../lib/strings");

function printMap(data) {
  console.log(data.join("\n"));
  console.log("\n");
}

const directions = {
  "^": [0, -1],
  ">": [1, 0],
  v: [0, 1],
  "<": [-1, 0],
};
const turnDirections = {
  "^": ">",
  ">": "v",
  v: "<",
  "<": "^",
};

function findGuard(data) {
  for (let y = 0; y < data.length; y++) {
    const upGuard = data[y].indexOf("^");
    const rightGuard = data[y].indexOf(">");
    const downGuard = data[y].indexOf("v");
    const leftGuard = data[y].indexOf("<");

    if (upGuard !== -1) {
      return [upGuard, y];
    }
    if (rightGuard !== -1) {
      return [rightGuard, y];
    }
    if (downGuard !== -1) {
      return [downGuard, y];
    }
    if (leftGuard !== -1) {
      return [leftGuard, y];
    }
  }
}

function nextPositionIsInBounds(data, currentPosition, guardDirection) {
  const [x, y] = currentPosition;
  const [dx, dy] = directions[guardDirection];
  const nextPosition = [x + dx, y + dy];

  const [tx, ty] = nextPosition;
  return tx >= 0 && ty >= 0 && tx < data[y].length && ty < data.length;
}

function nextPositionIsObstacle(data, currentPosition, guardDirection) {
  const [x, y] = currentPosition;
  const [dx, dy] = directions[guardDirection];
  const nextPosition = [x + dx, y + dy];

  const [tx, ty] = nextPosition;
  return data[ty][tx] === "#";
}

function turnGuard(data, currentPosition, currentGuardDirection) {
  const [x, y] = currentPosition;
  const newDirection = turnDirections[currentGuardDirection];
  data[y] = replaceCharacter(data[y], newDirection, x);
  return newDirection;
}

function moveGuard(data, currentPosition, currentGuardDirection) {
  const [x, y] = currentPosition;
  const [dx, dy] = directions[currentGuardDirection];
  const targetPosition = [x + dx, y + dy];
  const [tx, ty] = targetPosition;

  data[y] = replaceCharacter(data[y], "X", x);

  data[ty] = replaceCharacter(data[ty], currentGuardDirection, tx);
  return targetPosition;

  return false;
}

function part1(data) {
  const initialGuardPosition = findGuard(data);
  const [ix, iy] = initialGuardPosition;
  const initialGuardDirection = data[iy][ix];

  let guardPosition = initialGuardPosition;
  let guardDirection = initialGuardDirection;

  printMap(data);
  do {
    let i = 0;
    // Turn guard until he's not facing an object
    while (nextPositionIsObstacle(data, guardPosition, guardDirection)) {
      i++;
      guardDirection = turnGuard(data, guardPosition, guardDirection);
      // To avoid infinite spins
      if (i > 10) return "Spinning forever";
    }
    guardPosition = moveGuard(data, guardPosition, guardDirection);
  } while (nextPositionIsInBounds(data, guardPosition, guardDirection)); // moveGuard will return false once the guard is outside the map
  const finalGuardPosition = guardPosition;
  const [x, y] = finalGuardPosition;
  data[y] = replaceCharacter(data[y], "X", x);
  printMap(data);
  return data.join("\n").replace(/[^X]/g, "").length;
}

function part2(data) {}

module.exports = {
  part1,
  part2,
};
