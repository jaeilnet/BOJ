# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

def abc(n):
  result = 1
  if n > 0:
    result = n * abc(n-1)
  return result

n = int(input())
print(abc(n))