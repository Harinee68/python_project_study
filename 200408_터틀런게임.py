# 터틀런 게임

# 게임이 시작되면 키보드 방햐키를 이용하여 거북이를 움직인다.
# 주인공 거북이를 쫓아오는 빨간색 악당 거북이를 피해 초록색 동그라미 먹이를 최대한 많이 먹으면 됨.
# 도망치다가 악당 거북이에게 붙잡히면 게임 끝

import turtle as t
import random

score = 0
playing = False


t2 = t.Turtle() #악마 거북이 생성
t2.shape("turtle")
t2.color("red")
t2.speed(0)
t2.up()
t2.goto(0,200)

t3 = t.Turtle() #먹이 생성
t3.shape("circle")
t3.color("green")
t3.speed(0)
t3.up()
t3.goto(0,-200)

def turn_up(): #t가 위로 방향을 바라보게 만든다. 
    t.setheading(90)
    
def turn_down(): #t가 아래로 방향을 바라보게 만든다. 
    t.setheading(270)

def turn_right(): #t가 오른쪽으로 방향을 바라보게 만든다. 
    t.setheading(0)

def turn_left(): #t가 왼쪽으로 방향을 바라보게 만든다. 
    t.setheading(180)

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()

def play(): #게임 실행 함수
    global score
    global playing
    
    t.forward(10) #거북이가 10만큼 전진
    
    if random.randint(1,5) == 3:
        ang = t2.towards(t.pos()) #t2가 t를 바라보는 각도를 구함
        t2.setheading(ang) #t2의 각도를 ang로 바꿈
    speed = score + 5

    if speed > 15:
        speed = 15
    t2.forward(speed)
    if t.distance(t2) < 12:
        #게임종료
        text = "Score : " + str(score)
        message("Game Over", text)
        playing = False
        score = 0
    if t.distance(t3) < 12: #거북이가 먹이를 먹었을 때
        score += 1 #점수 추가
        t.write(score)
        t3_x = random.randint(-230,230) #랜덤으로 x좌표 위치 정함
        t3_y = random.randint(-230,230) #랜덤으로 y좌표 위치 정함
        t3.goto(t3_x, t3_y) #랜덤으로 정한 좌표로 t3 보냄
    if playing:
        t.ontimer(play, 100)

        
def message(m1,m2):
    t.clear()
    t.goto(0,100)
    t.write(m1, False, "center", ("",20))
    t.goto(0,-100)
    t.write(m2, False, "center", ("",15))
    t.home()


t.title("Turtle Run!")
t.setup(500,500)
t.bgcolor("orange")
t.color("white")
t.shape("turtle")
t.speed(0)

t.up()

t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")
t.onkeypress(start, "space")

t.listen()

message("Turtle Run", "[Space]")
