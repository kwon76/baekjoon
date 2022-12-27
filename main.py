#11399번 atm

"""
그리디 알고리즘에 따라 
사람들이 인출하는 데 걸리는 시간을 오름차순으로 정렬하면
각 사람이 인출하는데 필요한 시간의 합을 최소로 만들 수 있다.
"""
n = int(input())
lst = list(map(int, input().split()))

min_list = sorted(lst)
min_sum = 0
for i in range(n):
  min_sum += sum(min_list[:(i+1)])

print(min_sum)
