const readline = require("readline")
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

let input = []
let color = [
  "black",
  "brown",
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "violet",
  "grey",
  "white",
]

rl.on("line", (line) => {
  input.push(line)
})

rl.on("close", () => {
  let a = color.indexOf(input[0])
  let b = color.indexOf(input[1])

  let result = (String(a) + String(b)) * 10 ** color.indexOf(input[2])

  console.log(result)
})
