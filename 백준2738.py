#2738번 행렬 덧셈
n, m = map(int, input().split()) #행렬의 크기 

A, B = [], []

for i in range(n):
  row = list(map(int, input().split()))
  A.append(row)

for i in range(n):
  row = list(map(int, input().split()))
  B.append(row)

for i in range(n):
  for j in range(m):
    print(A[i][j] + B[i][j], end = ' ')
  print()
