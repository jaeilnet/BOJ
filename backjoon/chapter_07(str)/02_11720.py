# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# 입력 예제
# 5
# 54321

# 출력 예제
# 15

# 입력 예제2
# 25
# 7000000000000000000000000

# 출력예제2
# 7

n = input()

print(sum(map(int, input())))


# n = input()

# nums = input()
# total = 0
# for i in nums:
#   print(i)
#   total += int(i)
# print(total)