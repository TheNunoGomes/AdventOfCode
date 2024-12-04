function directionsToCheckP1(lastColIndex, lastRowIndex, [x, y]) {
  const charsLeft = 3;
  const directions = [];

  // Up
  if (y >= charsLeft) {
    directions.push("up");
  }

  // Up Right
  if (y >= charsLeft && lastColIndex - x >= charsLeft) {
    directions.push("upRight");
  }

  // Right
  if (lastColIndex - x >= charsLeft) {
    directions.push("right");
  }

  // Down Right
  if (lastRowIndex - y >= charsLeft && lastColIndex - x >= charsLeft) {
    directions.push("downRight");
  }

  //Down
  if (lastRowIndex - y >= charsLeft) {
    directions.push("down");
  }

  // Down Left
  if (lastRowIndex - y >= charsLeft && x >= charsLeft) {
    directions.push("downLeft");
  }

  // Left
  if (x >= charsLeft) {
    directions.push("left");
  }

  // Up Left
  if (x >= charsLeft && y >= charsLeft) {
    directions.push("upLeft");
  }

  return directions;
}

const dirs = {
  up: [0, -1],
  upRight: [1, -1],
  right: [1, 0],
  downRight: [1, 1],
  down: [0, 1],
  downLeft: [-1, 1],
  left: [-1, 0],
  upLeft: [-1, -1],
};

function checkLetter(charList, charCoordinates, letter) {
  const [x, y] = charCoordinates;

  if (charList[y][x] === letter) {
    return [x, y];
  }

  return false;
}

module.exports = {
  checkLetter,
  directionsToCheckP1,
  dirs,
};
