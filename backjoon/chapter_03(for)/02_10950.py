#  두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오


# 입      출
#  5         
#  1 1      2
#  2 3      5
#  3 4      7
#  9 8      17 
#  5 2      7

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(A+B)