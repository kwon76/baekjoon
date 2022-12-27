#10809번 알파벳 찾기
from string import ascii_lowercase
str = input()
#리스트를 -1로 초기화하고 a~z까지 26개이므로 26크기의 리스트 설정 한 후 str[i]일 때 처음으로 문자 a(임의)가 나왔다면 i를 -1짜리 리스트에 갱신
#알파벳 리스트 : https://angelplayer.tistory.com/193

ans = [-1]*26 #정답 리스트
alp = list(ascii_lowercase)

for i in range(len(alp)): 
#0~25까지
  for j in range(len(str)):
    #str안의 문자들
    #중복 문자는 어떻게?
    #ex) baekjoon 에서 o가 2개있으므로 alp[i] = o일때 -> ans[i]가 -1이 아니라면 j로 갱신을 안하면 됌
    if str[j] == alp[i]:
      if ans[i] == -1:
        ans[i] = j

for i in ans:
  print(i, end=" ")



#더 짧은 코드
# S = input()
# abc ='abcdefghijklmnopqrstuvwxyz'

# for i in abc:
#     if i in S:
#         print(S.index(i), end= ' ')
#     else:
#         print( -1, end =' ')
