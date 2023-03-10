#20363번 당근 키우기

x, y = map(int, input().split())

print(max(x, y) + min(x, y)//10 + min(x, y))