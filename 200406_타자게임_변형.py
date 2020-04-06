#타자게임 변형, 영어 단어를 보고 뜻을 입력

import random
import time

#대응하는 영어 단어와 뜻은 리스트의 인덱스가 같다.
lst = ["cat, 3단어", "dog, 1단어", "fox, 2단어", "monkey, 3단어",
       "mouse, 1단어", "panda, 2단어", "frog, 3단어", "snake, 1단어", "wolf, 2단어"] #영어 단어 리스트, 힌트로 뜻의  단어 개수를 알려줌
kor = ["고양이", "개", "여우", "원숭이", "쥐", "판다", "개구리", "뱀", "늑대"] #뜻 리스트

n = 1
num = int(input("풀 문제의 개수를 입력하세요=>")) #문제 개수 입력 받음

input("[타자게임] 준비되면 엔터!")
start = time.time() #시간 시작

lst_num = random.randint(0,7) #0에서 7까지의 랜덤번호

cor = lst[lst_num] 
    
while n <= num: #n이 num보다 작거나 같을 때 까지 반복
    print("*문제", n)
    print(cor)
    ans = input()
    if kor[lst_num] == ans: #뜻과 입력한 뜻이 같을 때
        print("통과!")
        n += 1
        lst_num = random.randint(0,7)
        cor = lst[lst_num]
    else: #뜻과 입력한 뜻이 다를 때
        print("오타! 다시 도전!")

end = time.time() #시간 끝

tme = end - start
tme = format(tme, ".2f") #소수점 둘째 자리까지 표기하게 하는 함수.

print("타자 시간:",tme,"초")
        
        
    
