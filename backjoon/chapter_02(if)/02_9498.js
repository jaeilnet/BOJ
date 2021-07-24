// 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var a = parseInt(input[0]);
// var b = parseInt(input[1]);


function solution(a) {
  if(a>=90) console.log("A")
  else if(a>=80) console.log("B")
  else if(a>=70) console.log("C")
  else if(a>=60) console.log("D")
  else console.log("F")
}

solution(a)