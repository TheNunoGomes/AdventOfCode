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

  const replacementChar = Number(data[y][x])
    ? `${Number(data[y][x]) + 1}`
    : "1";

  if (replacementChar === 4) {
    return true;
  }

  data[y] = replaceCharacter(data[y], replacementChar, x);
  data[ty] = replaceCharacter(data[ty], currentGuardDirection, tx);
  return targetPosition;
}

function tickGuard(data, guardPosition, guardDirection) {
  let i = 0;
  // Turn guard until he's not facing an object
  while (nextPositionIsObstacle(data, guardPosition, guardDirection)) {
    i++;
    guardDirection = turnGuard(data, guardPosition, guardDirection);
    // To avoid infinite spins
    if (i > 10) return "Spinning forever";
  }
  guardPosition = moveGuard(data, guardPosition, guardDirection);
  return [guardPosition, guardDirection];
}

function part1(data) {
  const initialGuardPosition = findGuard(data);
  const [ix, iy] = initialGuardPosition;
  const initialGuardDirection = data[iy][ix];

  let guardPosition = initialGuardPosition;
  let guardDirection = initialGuardDirection;

  do {
    [guardPosition, guardDirection] = tickGuard(
      data,
      guardPosition,
      guardDirection
    );
  } while (nextPositionIsInBounds(data, guardPosition, guardDirection)); // moveGuard will return false once the guard is outside the map
  const finalGuardPosition = guardPosition;
  const [x, y] = finalGuardPosition;
  data[y] = replaceCharacter(data[y], "X", x);
  return data.join("\n").replace(/[^X]/g, "").length;
}

async function part2(data) {
  let loopsFound = 0;
  const realMap = [...data];

  let guardPosition = findGuard(realMap);
  const [ix, iy] = guardPosition;
  let guardDirection = realMap[iy][ix];

  do {
    console.log("Real Map");
    printMap(realMap);

    await waitForInput("");
    const loopCheckMap = [...realMap];
    let loopCheckPosition = guardPosition;
    let loopCheckDirection = guardDirection;

    // Check if placing an obstacle in front causes a loop
    do {
      console.log("Loop Map");
      printMap(loopCheckMap);
      await waitForInput("");
      const tick = tickGuard(
        loopCheckMap,
        loopCheckPosition,
        loopCheckDirection
      );
      if (tick === true) {
        loopsFound++;
        break;
      }

      [loopCheckPosition, loopCheckDirection] = tick;
    } while (
      nextPositionIsInBounds(
        loopCheckMap,
        loopCheckPosition,
        loopCheckDirection
      )
    ); // moveGuard will return false once the guard is outside the map

    [guardPosition, guardDirection] = tickGuard(
      realMap,
      guardPosition,
      guardDirection
    );
  } while (nextPositionIsInBounds(realMap, guardPosition, guardDirection)); // moveGuard will return false once the guard is outside the map
  const finalGuardPosition = guardPosition;
  const [x, y] = finalGuardPosition;
  realMap[y] = replaceCharacter(realMap[y], "X", x);
  return loopsFound;
}

module.exports = {
  part1,
  part2,
};

const waitForInput = (query) => {
  return new Promise((resolve) => {
    process.stdout.write(query); // Display the query message
    process.stdin.resume(); // Start listening for input
    process.stdin.setEncoding("utf8"); // Ensure the input is a string

    process.stdin.on("data", (data) => {
      process.stdin.pause(); // Stop listening for input
      resolve(data.trim()); // Resolve the promise with trimmed input
    });
  });
};
