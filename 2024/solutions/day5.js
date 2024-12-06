function moveArrayElement(array, fromIndex, toIndex) {
  const element = array.splice(fromIndex, 1)[0];
  array.splice(toIndex, 0, element);
  return array;
}

function buildRulesMap(rules) {
  const rulesMap = {};

  rules.forEach(([page1, page2]) => {
    if (!rulesMap[page1]) {
      rulesMap[page1] = [];
    }
    rulesMap[page1].push(page2);
  });

  return rulesMap;
}

function fixSequence(rulesMap, sequence) {
  for (let i = 0; i < sequence.length; i++) {
    const currentPage = sequence[i];
    const pagesRight = sequence.slice(i + 1);

    for (let j = 0; j < pagesRight.length; j++) {
      const pageRight = pagesRight[j];
      if (
        !rulesMap[currentPage] ||
        !rulesMap[currentPage].includes(pageRight)
      ) {
        //This is the digit we need to fix
        sequence = moveArrayElement(
          sequence,
          sequence.indexOf(pageRight),
          sequence.indexOf(currentPage)
        );
      }
    }
  }
  const fixedSequence = sequence;
  return fixedSequence;
}

function part1(data) {
  const [rulesString, pageSequencesString] = data.join("\n").split("\n\n");
  const rules = rulesString.split("\n").map((rule) => rule.split("|"));
  const pageSequences = pageSequencesString
    .split("\n")
    .map((pageSequence) => pageSequence.split(","));
  const rulesMap = buildRulesMap(rules);
  const sequencesToSum = [];

  for (let k = 0; k < pageSequences.length; k++) {
    const pageSequence = pageSequences[k];

    let ruleBroken = false;
    for (let i = 0; i < pageSequence.length; i++) {
      const currentPage = pageSequence[i];
      const pagesRight = pageSequence.slice(i + 1);

      const rulesBroken = pagesRight.some((pageRight) => {
        return (
          !rulesMap[currentPage] || !rulesMap[currentPage].includes(pageRight)
        );
      });
      if (rulesBroken) {
        ruleBroken = true;
        break;
      }
    }
    if (!ruleBroken) {
      sequencesToSum.push(pageSequence);
    }
  }
  return sequencesToSum.reduce((sum, sequence) => {
    return sum + Number(sequence[(sequence.length - 1) / 2]);
  }, 0);
}

function part2(data) {
  const [rulesString, pageSequencesString] = data.join("\n").split("\n\n");
  const rules = rulesString.split("\n").map((rule) => rule.split("|"));
  const pageSequences = pageSequencesString
    .split("\n")
    .map((pageSequence) => pageSequence.split(","));
  const rulesMap = buildRulesMap(rules);

  let sequencesToFix = [];

  for (let k = 0; k < pageSequences.length; k++) {
    const pageSequence = pageSequences[k];

    for (let i = 0; i < pageSequence.length; i++) {
      const currentPage = pageSequence[i];
      const pagesRight = pageSequence.slice(i + 1);

      const rulesBroken = pagesRight.some((pageRight) => {
        return (
          !rulesMap[currentPage] || !rulesMap[currentPage].includes(pageRight)
        );
      });
      if (rulesBroken) {
        sequencesToFix.push(pageSequence);
        break;
      }
    }
  }
  let sequencesThatStillNeedFixing;
  do {
    sequencesToFix = sequencesToFix.map((sequence) =>
      fixSequence(rulesMap, sequence)
    );

    sequencesThatStillNeedFixing = [];

    for (let k = 0; k < sequencesToFix.length; k++) {
      const pageSequence = sequencesToFix[k];

      for (let i = 0; i < pageSequence.length; i++) {
        const currentPage = pageSequence[i];
        const pagesRight = pageSequence.slice(i + 1);

        const rulesBroken = pagesRight.some((pageRight) => {
          return (
            !rulesMap[currentPage] || !rulesMap[currentPage].includes(pageRight)
          );
        });
        if (rulesBroken) {
          sequencesThatStillNeedFixing.push(sequencesToFix);
          break;
        }
      }
    }
  } while (sequencesThatStillNeedFixing.length);

  return sequencesToFix.reduce((sum, sequence) => {
    return sum + Number(sequence[(sequence.length - 1) / 2]);
  }, 0);
}

module.exports = {
  part1,
  part2,
};
