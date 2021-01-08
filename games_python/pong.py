#!/usr/bin/env python3
import turtle
import os

window = turtle.Screen()
window.title('Pong by dlscoccia \o/')
window.bgcolor('white')
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('green')
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=4, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('green')
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=4, stretch_len=1)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# Moving functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")



# game loop
while True:
    window.update()

    # Ball moving
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bouncing check

    # top check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay dream.mp3")

    # bottom check
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # right check
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # left check
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Collisions handle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
