import random
import time

lst = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"] #게임에 나올 단어 리스트

n = 1
num = int(input("풀 문제의 개수를 입력하세요=>")) #문제 개수 입력 받음

input("[타자게임] 준비되면 엔터!")
start = time.time() #시간 시작

cor = random.choice(lst)
    
while n <= num: #n이 num보다 작거나 같을 때 까지 반복
    print("*문제", n)
    print(cor)
    ans = input()
    if cor == ans: #문제와 입력한 값이 같을 때
        print("통과!")
        n += 1
        cor = random.choice(lst)
    else: #문제와 입력한 값이 다를 때
        print("오타! 다시 도전!")

end = time.time() #시간 끝

tme = end - start
tme = format(tme, ".2f") #소수점 둘째 자리까지 표기하게 하는 함수.

print("타자 시간:",tme,"초")
        
        
    
