# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

# 입력
# 입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다. 각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.

# 출력
# 각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.



# while True:
#   n = list(map(int, input().split()))
#   m = []

#   for i in range(len(n)):
#     if n[i] % 3 == 0 or n[i] % 4 == 0 or n[i] % 5 == 0 :
#       m.append(True)
#     else:
#       m.append(False)

#   if False in m:
#     print("wrong")
#   elif n.count(0):
#     break
#   else:
#     print("right")

#  실패사유 3:4:5 비율만 피타고라스 인줄알고 5 10 13에서 틀림

while True:
        a = list(map(int, input().split()))
        max_num = max(a)
        if sum(a) == 0:
                break
        a.remove(max_num)
        if a[0] ** 2 + a[1] ** 2 == max_num ** 2:
                print('right')
        else:
                print('wrong')