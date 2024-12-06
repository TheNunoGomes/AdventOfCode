function replaceCharacter(targetString, newCharacter, index) {
  return (
    targetString.substring(0, index) +
    newCharacter +
    targetString.substring(index + 1)
  );
}

module.exports = {
  replaceCharacter,
};
