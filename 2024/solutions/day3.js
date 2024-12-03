function part1(data) {
  const corrupted = data.join('')
  let sumOfMuls = 0;

  let muls = corrupted.match(/(mul\([0-9]+,[0-9]+\))/g)
  muls = muls.map(mul => mul.replace('mul(', '').replace(')', '').split(','))
  muls.forEach(mul => {
    sumOfMuls += Number(mul[0]) * Number(mul[1])
  })

  return sumOfMuls;
}
function part2(data) {
  const dos = []
  const corrupted = data.join('\n')

  const splitLine = corrupted.split("don't()")

  dos.push(splitLine.shift())
  
  for(let j = 0; j < splitLine.length; j++) {
    const splitLineSegment = splitLine[j].split('do()');
    splitLineSegment.shift() // shift the don't (first element)
    dos.push(...splitLineSegment) // push the do's
  }

  return part1(dos)
}

module.exports = {
  part1,
  part2,
};
