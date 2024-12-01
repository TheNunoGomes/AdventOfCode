function parseLists(data) {
  const list1 = [];
  const list2 = [];
  data.forEach((line) => {
    const [num1, num2] = line.split("   ");
    list1.push(Number(num1));
    list2.push(Number(num2));
  });
  return [list1, list2];
}

function part1(data) {
  const [list1, list2] = parseLists(data);

  const sortedList1 = list1.sort();
  const sortedList2 = list2.sort();

  let distance = 0;
  for (let i = 0; i < sortedList1.length; i++) {
    distance += Math.abs(sortedList1[i] - sortedList2[i]);
  }
  return distance;
}

function part2(data) {
  const [list1, list2] = parseLists(data);
  let similarity = 0;
  list1.forEach((num1) => {
    similarity += num1 * list2.filter((num2) => num1 === num2).length;
  });

  return similarity;
}

module.exports = {
  part1,
  part2,
};
