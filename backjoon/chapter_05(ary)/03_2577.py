# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

# 입력 의 합 17037300
# 기대 출력 값 3, 1, 0, 2, 0, 0, 2, 0, 0 (0이 3번 1이 1번 2가 0번 3이 2번 이런 식으로 9까지 쓰인 횟수)


a = int(input())
b = int(input())
c = int(input())

abc = list(str(a*b*c))

for i in range(10):
  print(abc.count(str(i)))