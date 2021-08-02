# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 
# 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 예제 입력 1 
# 3
# happy
# new
# year

# 예제 출력 1 
# 3

# 연속단어만 찾아서 몇개인지 출력함. 연속단어란 a 라는 문자가 연속해서 쓰여야함, aabbb, 아닌경우 aaabaaa



T = int(input())

answer = 0
for i in range(T):
  S = input()
  cnt = 0
  for j in range(len(S)-1):
    if S[j] != S[j+1]:
      newWord = S[j+1:]
      if newWord.count(S[j]):
        cnt += 1
  if cnt == 0:
    answer += 1
print(answer)