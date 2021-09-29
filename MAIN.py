from turtle import Turtle,Screen
import time
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


def go_up():
    paddle.forward(30)

def go_down():
    paddle.back(30)

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Break Out game")

#make puddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0,-200)
screen.listen()
screen.onkey(go_down,"Left")
screen.onkey(go_up, "Right")


#ball
ball = Turtle()
ball.color("white")
ball.shape("circle")
ball.penup()
x_move = 10
y_move = 10

all_blocks = []
hod = 0

brickss = 0

score = 0

scores = Turtle()
scores.color('white')
style = ('Courier', 10, 'italic')
scores.penup()
scores.goto(100,-250)
scores.write(f'score:{score}', font=style, align='right')
scores.hideturtle()
#blocks
for i in range(70):
    if i > 0 and i < 14:
        hod += 42
        new_block = Turtle("square")
        new_block.shapesize(stretch_wid=1,stretch_len=2)
        new_block.color(random.choice(COLORS))
        new_block.penup()
        new_block.goto(-300+hod,270)
        all_blocks.append(new_block)
    elif i == 14:
        hod = 0
    elif i > 14 and i < 28:
        hod += 42
        new_block = Turtle("square")
        new_block.shapesize(stretch_wid=1,stretch_len=2)
        new_block.color(random.choice(COLORS))
        new_block.penup()
        new_block.goto(-300+hod,250)
        all_blocks.append(new_block)
    elif i == 28:
        hod = 0
    elif i > 28 and i < 42:
        hod += 42
        new_block = Turtle("square")
        new_block.shapesize(stretch_wid=1, stretch_len=2)
        new_block.color(random.choice(COLORS))
        new_block.penup()
        new_block.goto(-300 + hod, 230)
        all_blocks.append(new_block)
    elif i == 42:
        hod = 0
    elif i > 42 and i < 56:
        hod += 42
        new_block = Turtle("square")
        new_block.shapesize(stretch_wid=1, stretch_len=2)
        new_block.color(random.choice(COLORS))
        new_block.penup()
        new_block.goto(-300 + hod, 210)
        all_blocks.append(new_block)

    elif i == 56:
        hod = 0
    elif i > 56 and i < 70:
        hod += 42
        new_block = Turtle("square")
        new_block.shapesize(stretch_wid=1, stretch_len=2)
        new_block.color(random.choice(COLORS))
        new_block.penup()
        new_block.goto(-300 + hod, 190)
        all_blocks.append(new_block)








def move():
    new_x = ball.xcor() - x_move
    new_y = ball.ycor() - y_move
    ball.goto(new_x, new_y)

def bounce_y():
    global y_move
    y_move *= -1

def bounce_x():
    global x_move
    x_move *= -1


def reset_position():
        global x_move
        ball.goto(0,0)
        x_move *= -1

def refresh_score():
    global scores
    scores.reset()
    scores = Turtle()
    scores.color('white')
    style = ('Courier', 10, 'italic')
    scores.penup()
    scores.goto(100, -250)
    scores.write(f'score:{score}', font=style, align='right')
    scores.hideturtle()






game_is_true = True
while game_is_true:
    time.sleep(0.1)
    screen.update()
    move()
    for brick in all_blocks:
        if brick.distance(ball)  < 20:
            brick.reset()
            bounce_y()
            score +=1
            brickss +=1
            refresh_score()

    if ball.distance(paddle) < 30 and ball.ycor() > -270:
            bounce_y()
    elif ball.xcor() < -270:
        bounce_x()
    elif ball.xcor() > 270:
        bounce_x()
    elif ball.ycor() > 270:
        bounce_y()
    elif ball.ycor() < -280 and ball.distance(paddle) > 50:
        game_over = Turtle()
        game_over.color('white')
        style = ('Courier', 30, 'italic')
        game_over.write(f'Game Over!Your score is {score}', font=style, align='center')
        game_over.hideturtle()
        game_is_true = False
    elif brickss > 62:
        game_over = Turtle()
        game_over.color('white')
        style = ('Courier', 30, 'italic')
        game_over.write(f'Game Over!Your score is {score}', font=style, align='center')
        game_over.hideturtle()
        game_is_true = False














screen.exitonclick()