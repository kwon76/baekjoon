#16433번 주디와 당근 농장

n, r, c = map(int, input().split())

a = [['.' for col in range(n)] for row in range(n)]
for i in range(n):
  for j in range(n):
    if (r+c)%2 == 0:
      if (i+j)%2 == 0:
        a[i][j] = 'v'
    else:
      if (i+j)%2 == 1:
        a[i][j] = 'v'

for i in range(len(a)):            
    for j in range(len(a[i])):    
        print(a[i][j], end = '')
    print()