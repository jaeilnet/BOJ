var fs = require("fs")

// 문자 하나
var input = fs.readFileSync("/dev/stdin").toString()

// 한 칸 띄어쓰기로 구분
// input[0], input[1] 배열에서 꺼내쓰면 된다.
var input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")

// 줄바꿈으로 구분
var input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")

// 만약 인풋값이 숫자라면
var input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map(function(a) {
    return +a
  })

// readline
  const readline = require("readline");
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  let input = [];
  
  rl.on("line", function (line) {
    input.push(parseInt(line));
  }).on("close", function () {
    ///////////////////////////////
    const a = input[0];
    const b = input[1];

    process.exit();
});