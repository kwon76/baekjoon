#1065번 한수

num = int(input())
  #브루트포스 알고리즘
  #1. N의 각 자리 숫자를 리스트로 만든다
  #2. 리스트가 등차수열을 이루는지 확인한다.
  #3. 한수이면 cnt +1 
def isHansu(N):
  lst = []
  while(N!=0):
    lst.append(N%10)
    N = N // 10

  #lst = 일의자리부터 맨앞자리까지 담김
  for i in range(2, len(lst)):
    if lst[i-1] -lst[i-2] != lst[i]-lst[i-1]:
      return False

  return True
"""ex) 1000
lst = [0, 0, 0, 1]
len(lst) = 4
i = 2 lst[1]-lst[0]=lst[2]-lst[1]
i = 3 lst[2]-lst[1]-lst[3]-lst[2]"""

cnt = 0
for i in range(1, num + 1):
  if isHansu(i):
    cnt += 1

# print(isHansu(num))
print(cnt)
