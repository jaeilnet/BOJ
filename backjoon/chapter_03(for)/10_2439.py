# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 하지만 역순으로 출력한다.

T = int(input())

for i in range(1, T+1):
  for j in range(T-i):
    print(" ", end="")
  print(i*"*")