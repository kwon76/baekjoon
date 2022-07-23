#1837번 암호제작
"""
비밀 키 : 임의의 두 소수 p와 q의 곱 pq
이때 p와 q 둘 중 어느 하나라도 임의의 k보다 작디면 '좋지 않은 암호'로 간주
"""
n, k = map(int, input().split())
#n : 비밀 키(p*q), k : 좋음 여부의 기준 수
#n을 소인수분해 한뒤 그 중 작은 소수와 k를 비교하여 출력하자.
#이때, 좋지 않음 암호라면 작은 소수를 출력하자.

# #소인수분해
# #1. 에라토스테네스의 체
# def eratosthenes(m):
#   sieve = [True] * m
#   for i in range(2, m):
#     if sieve[i] == True:
#       for j in range(i+i, m, i):
#         sieve[j] = False
#   return [i for i in range(2, m) if sieve[i] == True]

# #2. 소인수분해
# def primeFactor(a):
#   lst = eratosthenes(a+1) #a보다 작거나 같은 모든 소수를 원소로 가지는 리스트

#   i = 0
#   result = []
#   while i < len(lst):
#     if(a % lst[i] == 0):
#       result.append(lst[i])
#       a /= lst[i]
#     else:
#       i += 1
#   return result #a의 소인수들이 들어있는 리스트 출력됨
# #이 문제의 경우 무조건 두 소수의 곱이므로 result안에는 작은 소수와 큰 소수가 차례로 들어있을 것

# #3. 비교 및 출력
# if primeFactor(n)[0] >= k:
#   print("GOOD")
# else:
#   print("BAD "+str(primeFactor(n)[0]))

#위의 시도는 런타임 에러(OverflowError 출력) 

"""
정답 풀이
k보다 작은 n의 소인수를 찾기만 하면 된다! 관점 전환1
어차피 암호는 두 소수의 곱이므로 두 소수외의 다른 수들로는 나누어떨어지지 않으므로
for i in range(2, k)를 사용해도 무관하다! 관점 전환2
"""
a = True #좋음 여부 판단
for i in range(2, k):
  if n % i == 0: #나누어떨어졌을 경우 i는 무조건 소수이고, k보다 작으므로 좋지 않은 암호
    print("BAD "+str(i))
    a = False   
    break
if a:
  print("GOOD") #만약 a가 여전히 True라면, k보다 큰 소인수들로 이루어진 암호이므로 좋은 암호  
    

  
