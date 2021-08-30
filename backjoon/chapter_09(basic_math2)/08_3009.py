# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오

# 예제 입력 1 
# 5 5
# 5 7
# 7 5

# 예제 출력 1 
# 7 7

# 예제 입력 2 
# 30 20
# 10 10
# 10 20

# 예제 출력 2 
# 30 10

x_arr = []
y_arr = []

for _ in range(3):
  x, y = map(int, input().split())
  x_arr.append(x)
  y_arr.append(y)

for i in range(3):
  # print("x", x_arr.count(x_arr[i]))
  # print("y", y_arr.count(y_arr[i]))
  if x_arr.count(x_arr[i]) == 1:
    x4 = x_arr[i]
  if y_arr.count(y_arr[i]) == 1:
    y4 = y_arr[i]

print(x4, y4)