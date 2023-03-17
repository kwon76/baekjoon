#16208번 귀찮음

n = int(input())
li = sorted(list(map(int, input().split())))
# a = 0

# for i in range(n):
#   a += li[i] * sum(li[(i+1):])
# print(a)

a = sum(li)
ans = 0
for i in li:
  ans += i * (a - i)
  a -= i
print(ans)