# 이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 
# 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.


# 예제 입력 1 
# 14
# 예제 출력 1 
# 2/4


# n = input()
# for k in range(int(n)):
#   for i in range(1, 6, 1):
#     for j in range(1, 6, 1):
#       if i == j:
#         j+=1
#       elif i<j :
#         i+=2
#         j-=1
#       elif i>j:
#         i-=1
#         j+=1
#   print(f'{i}/{j}')
    

X=int(input())

line=1
while X>line:
    X-=line
    line+=1
    
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X
    
print(a, '/', b, sep='')

#포기