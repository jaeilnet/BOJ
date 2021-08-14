# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.


# 주어진 수들 중 소수의 개수를 출력한다.

# 예제 입력 1 
# 4
# 1 3 5 7
# 예제 출력 1 
# 3


t = int(input())
num = list(map(int, input().split()))

res = []

for i in range(t):
  cnt = 0
  for j in range(num[i]):
    if num[i] > 1 and num[i] % (j+1) == 0:
      cnt += 1
  if cnt == 2:
    res.append(num[i])
print(len(res))