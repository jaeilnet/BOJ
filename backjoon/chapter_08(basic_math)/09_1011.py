# Fly me to the Alpha Centauri
# https://www.acmicpc.net/problem/1011

# 각 테스트 케이스에 대해 x지점으로부터 y지점까지 정확히 도달하는데 필요한 최소한의 공간이동 장치 작동 횟수를 출력한다.

# 예제 입력 1 
# 3
# 0 3
# 1 5
# 45 50

# 예제 출력 1 
# 3
# 3
# 4

# 틀린코드
# import sys

# T = int(input())

# res = 0
# for i in range(T):
#   a, b = map(int, sys.stdin.readline().split())
#   res = ((b - a)-1)
#   if a == 0 or b == 0:
#     res += 1
#   print(res)


# 정답 코드

t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance :
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            move += 1  
    print(count)