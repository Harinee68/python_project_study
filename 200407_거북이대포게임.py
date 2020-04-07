import turtle as t
import random

def turn_up(): #각도를 올리는 함수
    t.left(2)

def turn_down(): #각도를 내리는 함수
    t.right(2)

def fire(): #대포를 발사하는 함수
    ang = t.heading()
    while t.ycor() > 0: #turtle의 y 좌표가 0을 넘으면 계속 반복
        t.forward(15)
        t.right(5)

    d = t.distance(target, 0) #turtle과 (target, 0)사이의 거리를 구함
    t.sety(random.randint(10,100)) #성공, 실패 글자를 띄울 y좌표값을 정함
    
    if d < 25: #turtle과 (target,0) 의 거리가 25보다 작을 때
        t.color("blue")
        t.write("Success!", False, "center", ("",15))
    else:
        t.color("red") #turtle과 (target,0)의 거리가 25보다 클 때
        t.write("Fail", False, "center", ("",15))

    t.color("black")
    t.goto(-200,10) #시작점으로 다시 돌아감
    t.setheading(ang) #시작할 때 각도로 다시 돌려놓음.


#게임 시작
t.goto(-300,0) 
t.goto(300,0)

target = random.randint(50,150) #target의 x좌표값을 정함.
t.pensize(3)
t.color("yellow") 
t.up()
#target을 그림
t.goto(target - 25, 2)
t.down()
t.goto(target + 25, 2)

t.color("black")
t.up()
t.goto(-200,10)
t.setheading(20)

t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")

t.listen() #turtle 그래픽 창이 키보드 입력을 받을 수 있도록 함.

    
        
