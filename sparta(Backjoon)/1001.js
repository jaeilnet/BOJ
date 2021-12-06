const fs = require("fs")
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `1
3 2
`
).split("\n")

const input = (() => {
  let line = 0
  return () => stdin[line++]
})()

let t = input()
while (t--) {
  const [a, b] = input().split(" ").map(Number)
  console.log(a - b)
}
