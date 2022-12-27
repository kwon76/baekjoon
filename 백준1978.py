#1978번 소수 찾기
n = int(input())
lst = map(int, input().split())
cnt = 0

def isPrime(n):

    if(n == 1): return False   

    for i in range(2, n):
        if(n % i == 0):
            return False
    
    return True
    

for i in lst:
  if isPrime(i):
    cnt += 1

print(cnt)