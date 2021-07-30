# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 입력 예제
# baekjoon

# 출력 예제
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1


S = input()
res = [-1]*26

for i in range(len(S)):
  if res[ord(S[i])-97] != -1:
    continue
  else:
    res[ord(S[i])-97] = i

for i in range(26):
  print(res[i], end="")

  