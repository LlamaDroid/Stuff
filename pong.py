#Python Pong Game, in Cyan XD

import turtle

wn = turtle.Screen()
wn.title("Cyan Pong by LlamaPantz")
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

#Left Paddle 
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color("cyan")
paddle_l.shapesize(stretch_wid=5, stretch_len=1)
paddle_l.penup()
paddle_l.goto(-350,0)

#Right Paddle
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("cyan")
paddle_r.shapesize(stretch_wid=5, stretch_len=1)
paddle_r.penup()
paddle_r.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("cyan")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1

def paddle_l_up():
	y = paddle_l.ycor()
	y += 20
	paddle_l.sety(y)
def paddle_l_down():
	y = paddle_l.ycor()
	y -= 20
	paddle_l.sety(y)
def paddle_r_up():
	y = paddle_r.ycor()
	y += 20
	paddle_r.sety(y)
def paddle_r_down():
	y = paddle_r.ycor()
	y -= 20
	paddle_r.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_l_up, "w")
wn.onkeypress(paddle_l_down, "s")
wn.onkeypress(paddle_r_up, "Up")
wn.onkeypress(paddle_r_down, "Down")


#Main game loop
while True:
	wn.update()

	#move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#border
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
	if ball.xcor() > 390:
		ball.goto(0,0)
		ball.dx *= -1
	if ball.xcor() < -390:
		ball.goto(0,0)
		ball.dx *= -1

	#paddle and ball colflision
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_r.ycor() + 40 and ball.ycor() > paddle_r.ycor() - 40):
		ball.setx(340)
		ball.dx *= -1
	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_l.ycor() + 40 and ball.ycor() > paddle_l.ycor() - 40):
		ball.setx(-340)
		ball.dx *= -1