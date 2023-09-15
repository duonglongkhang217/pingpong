import turtle
import pygame
import os


board = turtle.Screen()
board.title = "Pong"
board.bgcolor("Black")
board.setup(width=800, height=600)
board.tracer(0)

player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("White")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(-350, 0)

player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("White")
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.penup()
player_2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("White")
ball.penup()
ball.goto(0, 0)
BALL_SPEED = 0.2
ball.dx = BALL_SPEED
ball.dy = -BALL_SPEED

def player1_up():
    y = player_1.ycor()
    if y < (board.window_height() / 2) - 40:
        y += 20
    player_1.sety(y)

def player1_down():
    y = player_1.ycor()
    if y > -(board.window_height() / 2) + 40:
        y -= 20
    player_1.sety(y)

def player2_up():
    y = player_2.ycor()
    if y < (board.window_height() / 2) - 40:
        y += 20
    player_2.sety(y)

def player2_down():
    y = player_2.ycor()
    if y > -(board.window_height() / 2) + 40:
        y -= 20
    player_2.sety(y)

board.listen()
board.onkeypress(player1_up, "w")
board.onkeypress(player1_down, "s")
board.onkeypress(player2_up, "Up")
board.onkeypress(player2_down, "Down")

center_line = turtle.Turtle()
center_line.speed(0)
center_line.color("white")
center_line.penup()
center_line.goto(0, -300)
center_line.pendown()
center_line.pensize(5)
center_line.setheading(90)
while center_line.ycor() <= 300:
    center_line.forward(40)
    center_line.penup()
    center_line.forward(40)
    center_line.pendown()

score_1 = 0
score_2 = 0

scr = turtle.Turtle()
scr.speed(0)
scr.color("White")
scr.penup()
scr.hideturtle()
scr.goto(0, 260)
scr.write("Player 1: 0                                        ", align="center", font=("Comic Sans MS", 24, "normal"))

scr2 = turtle.Turtle()
scr2.speed(0)
scr2.color("White")
scr2.penup()
scr2.hideturtle()
scr2.goto(0, 260)
scr2.write("                                       Player 2: 0", align="center", font=("Comic Sans MS", 24, "normal"))

# ...
border_left = -1090
border_right = 1090
while True:
    board.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    
    if ball.xcor() < border_left:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        scr2.clear()
        scr2.write("                                       Player 2: {}".format(score_2), align="center", font=("Comic Sans MS", 24, "normal"))

    
    if ball.xcor() > border_right:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        scr.clear()
        scr.write("Player 1: {}                                        ".format(score_1), align="center", font=("Comic Sans MS", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_2.ycor() + 50 and ball.ycor() > player_2.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        player_2_color = player_2.color()[0]
        ball.color(player_2_color)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player_1.ycor() + 50 and ball.ycor() > player_1.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        player_1_color = player_1.color()[0]
        ball.color(player_1_color)

