# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 에라토스테네스의 체로 풀어 봅시다.

def arr(num):
  if num == 1:
    return False
  else :
    for i in range(2, int(num**0.5)+1):
      if num % i == 0:
        return False
    return True

M,N = map(int, input().split())

for i in range(M, N+1):
  if arr(i):
    print(i)
    