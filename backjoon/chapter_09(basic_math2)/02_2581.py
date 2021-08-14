# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

# 예제 입력 1 
# 60
# 100
# 예제 출력 1 
# 620
# 61
# 예제 입력 2 
# 64
# 65
# 예제 출력 2 
# -1


m = int(input())
n = int(input())

res = []

for i in range(m, n+1):
  cnt =0
  for j in range(1, i+1):
    if i % j == 0:
      cnt += 1
      if cnt > 2:
        break;
  if cnt == 2:
    res.append(i)
if len(res) != 0:
  print(sum(res))
  print(res[0])
else:
    print("-1")
    