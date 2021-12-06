var fs = require("fs")
var input = fs.readFileSync("/dev/stdin").toString().split(" ")

var a = parseInt(input[0])
var b = parseInt(input[1])

function solution(a, b) {
  if (a > b) console.log(">")
  else if (a < b) console.log("<")
  else if (a === b) console.log("==")
  else false
}

solution(a, b)
