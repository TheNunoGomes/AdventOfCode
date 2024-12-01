const { solve } = require("./lib/solver");
const { validate } = require("./lib/validations");

const [_node, _file, ...args] = process.argv;

function getArgumentValues(args) {
  let day, part;
  let test = false;

  for (let i = 0; i < args.length; ) {
    const flag = args[i];
    if (["-d", "--day"].includes(flag)) {
      day = Number(args[i + 1]);
      i += 2;
    } else if (["-p", "--part"].includes(flag)) {
      part = Number(args[i + 1]);
      i += 2;
    } else if (["-t", "--test"].includes(flag)) {
      test = true;
      i++;
    } else {
      throw new Error(`Invalid parameter: ${args[i]}`);
    }
  }
  return { day, part, test };
}
try {
  validate(args);

  const { day, part, test } = getArgumentValues(args);

  solve(day, part, test);
} catch (e) {
  console.error(e.message);
}
