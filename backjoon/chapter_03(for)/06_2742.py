# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오. 거꾸로

T = int(input())

for i in range(T, 0, -1):
  print(i)

for i in range(T):
  print(T - i)

