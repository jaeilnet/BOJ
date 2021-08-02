# 위의 그림과 같이 육각형으로 이루어진 벌집이 있다.
# 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 
# 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 
# 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 
# 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 
# 계산하는 프로그램을 작성하시오. 
# 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.


# 내 코드 실패 -> 리팩토링

n = int(input())

cnt = 1
num = 1

while num <= n: 
    cnt += 1  
    num += cnt * 6
print(cnt)  


# n = int(input())

# nums_pileup = 1  # 벌집의 개수, 1개부터 시작
# cnt = 1
# while n > nums_pileup :
#     nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
#     cnt += 1  # 반복문을 반복하는 횟수
# print(cnt)

# 구글링 답지
# N = int(input())

# first = 1
# plus = 6
# room = 1

# if N == 1:
#   print(1)
# else:
#   while True:
#     first = first + plus
#     room+= 1
#     if N <= first:
#       print(room)
#       break
#     plus += 6

