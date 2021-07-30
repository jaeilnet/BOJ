# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.


# ex) 입  출
#     A   65 
#     C   67
#     0   48
#     9   57
#     z   122


T = input()

if type(T) == str:
  print(ord(T))  # 타입이 문자면 ord 아스키코드로 변환

elif type(T) == int:
  print(chr(T))  # 타입이 숫자면 chr 아스키코드로 변환