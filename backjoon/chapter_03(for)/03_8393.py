# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

T = int(input())


sum = 0
for i in range(T+1):
  sum = sum + i
 
print(sum)