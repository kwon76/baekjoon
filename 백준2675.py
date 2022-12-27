#2675번 문자열 반복
n = int(input())
for i in range(n):
  rep, word = input().split()
  for j in range(len(word)):
    print("%s" % (word[j]*int(rep)), end = '')
  print()

#퍼온 코드
# t = int(input())
# for i in range(t):
#     num, s = input().split()
#     text = ''
#     for i in s:
#         text += int(num) * i
#     print(text)