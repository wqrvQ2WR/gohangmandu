#고향만두야미
import time
import winsound
score = 0
list = []

input("""
교항먄듀 게임
2026.2.11.14:23:41.24
v1.0
시작하려면 enter누르쇼

""")

for i in range(5) :
    재료 = input('''
               














               





재료선택(5개, 중복 가능)
====================
(돼지고기),(양파),(스핔이)
,(마늘),(에이스),(고깃기름)
,(RAM),(CPU),(트랄랄렐로 트랄랄라)
====================
''')
    list.append(재료)

for i in range(5) :
    if list[i] == '돼지고기' :
        score += 3
    elif list[i] == '양파' :
        score += 2
    elif list[i] == '스핔이' :
        score -= 1
    elif list[i] == '마늘' :
        score += 2
    elif list[i] == '에이스' :
        score += 1
    elif list[i] == '고깃기름' :
        score += 1
    elif list[i] == 'RAM' :
        score -= 1
    elif list[i] == 'CPU' :
        score -= 2
    elif list[i] == '트랄랄렐로 트랄랄라' :
        score += 1
    else :
        print(list[i], '는(은)없는건데요')
print()
input("요리하기")
time.sleep(1)
print('.')
time.sleep(1)
print('..')
time.sleep(1)
print('...')
time.sleep(1)
print('....')
time.sleep(1)
print('.....')
time.sleep(1)
print('......')

if score >= 8 :
    print("성공!")
    print(score, end="점!")
elif score <= 7 :
    print("맛없어요")
    print(score, end='점...')