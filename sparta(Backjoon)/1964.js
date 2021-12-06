const readline = require("readline")

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

rl.on("line", (line) => {
  n = Number(line)
})

rl.on("close", () => {
  let sum = 0

  let cnt = 3

  for (let i = 1; i < n; i++) {
    sum += i * 5 - cnt
    cnt += 2
    console.log(sum)
  }

  sum += n * 5

  console.log(sum)
})
