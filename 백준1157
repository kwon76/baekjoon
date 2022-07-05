#1157번 단어 공부
from string import ascii_uppercase
word = input().upper()
#대소문자를 구별하지 않으므로 대문자로 다 만들어버린 후, count한다.
#알파벳 대문자를 list로 하는 alp_lst 생성
alp_lst = list(ascii_uppercase)
#alp_lst길이 만큼의 count용 리스트 생성
alp_cnt = [0]*len(alp_lst)

for i in range(len(alp_lst)):
  for j in range(len(word)):
    if word[j] == alp_lst[i]:
      alp_cnt[i] += 1

cnt_max = max(alp_cnt)
#갱신한 후 max값 선정 -> 후 max값이 알파벳 대문자 중 1개일 경우 그 문자 출력, 2개 이상일 경우 ?출력
if alp_cnt.count(cnt_max) == 1:
  print(alp_lst[alp_cnt.index(cnt_max)])
else:
  print('?')
