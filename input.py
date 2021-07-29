
# 1개의 입력 input 은 모두 문자열로 취급한다.

A = int(input())

# 공백을 기준으로 2개이상의 입력을 받을 때 5, 10

X = map(int, input().split())

# 공백을 기준으로 구분 된 데이터를 받을 때 ex) 1 3 4 5 2 3 4 5
A = list(map(int, input().split()))

# 좀 더 입력 빨리 받기

import sys

# 공백으로 구분 된 2개 숫자 입력 받기

N, M = map(int ,sys.stdin.readline().split())

# 2차원 리스트 입력 받기

board = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]

# 문자열 입력 받기

data = sys.stdin.readline().rstrip()

# f-string(3.6이상 사용가능) 리터럴방식?

answer = 5
print(f'정답은 {answer} 입니다.')

