#2869번 달팽이는 올라가고 싶다
a, b, v = map(int, input().split())
#a : 달팽이가 올라갈 수 있는 거리
#b : 달팽이가 미끄러져 내려가는 거리
#v : 나무 막대의 높이

"""
ex) a = 3, b = 1, v = 10
첫째날 3미터 올라가고 1미터 내려감(2)
둘쨰날 3미터 올라가고 1미터 내려감(4)
셋째날 3미터 올라가고 1미터 내려감(6)
넷째날 8
다섯째날 3미터 올라감 -> 끝(10)

달팽이가 d일째날 도착했다면
d-1날 까지는 (a-b)*(d-1)만큼 올라감
d일째날에 a가 v-(a-b)*(d-1)보다 크거나같음
"""
#첫번째 시도 : 시간 초과

# d = 0 #정답 변수
# while True:
#   d += 1 #하루가 시작
#   if a >= v - (a-b)*(d-1):
#     break #만약 올라간 만큼이 v-(a-b)*(d-1)보다 크거나 같다면 정상 도착
# print(d)

#시간을 단축하려면?

#종우씨의 힌트 : 나누기
"""
ex) a = 3, b = 1, v = 10
달팽이가 하루가 지날 때 마다 최종 변위는 2미터씩 증가함
마지막날에 10-3=7이므로 7/2=3.5 -> 4일+1(마지막날) = 5일
10/2 = 5이므로 5일
ex) a = 100, b = 99, v = 10000
달팽이가 하루가 지날 때 마다 최종 변위는 1미터씩 증가함
마지막날에 10000-100=9900이므로 9900/1=9900 -> 9900일+1(마지막날) = 9901일
ex) a = 70, b = 20, v = 5000
달팽이가 하루가 지날 때 마다 최종 변위는 50미터씩 증가함
마지막날에 5000-70=4930이므로 4930/50=98.6 -> 99일+1(마지막날) = 100일
=>
(v-a)/(a-b) -> 나머지가 0일 경우 d = (v-a)//(a-b) + 1 
               나머지가 0이 아닌 경우 d = (v-a)//(a-b) + 2
"""
if (v-a)%(a-b) == 0:
  print((v-a)//(a-b)+1)
else:
  print((v-a)//(a-b)+2)
  

