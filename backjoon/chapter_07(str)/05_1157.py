# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
#  단, 대문자와 소문자를 구분하지 않는다.

#입력예제

# Mississipi
# zZa
# z

#출력예제

# ?
# Z
# Z

S = input().upper()

setS = list(set(S))

cntt = []
for i in setS:
  cnt = S.count(i)
  cntt.append(cnt)
if cntt.count(max(cntt)) > 1:
  print("?")
else:
  max_index = cntt.index(max(cntt))
  print(setS[max_index])
      

      

