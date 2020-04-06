#랜덤으로 나오는 계산 문제의 정답, 오답 개수를 구하는 프로그램

import random

def make_question(): #문제를 문자열으로 출력하는 함수
    a = random.randint(1,40)
    b = random.randint(1,20)
    op = random.randint(1,3)

    q = str(a)

    if op == 1:
        q = q + "+" #문자열 연결도 '+' 연산자로
    if op == 2:
        q = q + "-"
    if op == 3:
        q = q + "*"

    q = q + str(b)

    return q


cor = 0 # 정답 개수 저장 변수
wro = 0 # 오답 개수 저장 변수

q_num = int(input("문제를 몇 개 푸시겠습니까? "))

for x in range(q_num): #q_num번 만큼 반복
    q = make_question()
    print(q)
    ans = input("=") #input()으로 입력된 변수는 다 문자열이다.
    r = int(ans) #그래서 계산하려면 int()로 바꿔줘야함

    if r == eval(q):
        cor += 1
        print("정답!")
    else:
        wro += 1
        print("오답!")

print("정답:",cor,"오답:",wro)

cor_rate = (cor/q_num)*100
print("정답률:",cor_rate, "%")

if cor_rate == 100:
    print("축하드립니다! 다 맞았습니다!")

