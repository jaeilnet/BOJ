// N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

var fs = require("fs")
var input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")

  let num = Number(input[0])

  for(let i = 1; i <= 9; i++){
    console.log(`${num} * ${i} =`,num * i)
  }