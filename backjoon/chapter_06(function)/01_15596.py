# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.



def solve(a):
  ans = 0
  for num in a:
    ans += num
  return ans

def solve(a):
  return sum(a)

# sum 이라는 함수는 a 안에 있는 걸 모두 더해준다.