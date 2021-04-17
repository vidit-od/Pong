import turtle

# pre-req:
speed = 0
gear = 1
start = True
width = 400
height = 300
scorea = 0
scoreb = 0

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(2*width, 2*height)
window.tracer(0)
# paddle 1
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(5, 1)
paddle_A.penup()
paddle_A.setposition(-width+50, 0)
# paddle 2

paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(5, 1)
paddle_B.penup()
paddle_B.setposition(width-50, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx = 0.5
ball.dy = 0.5

# paddle movement


def paddle_AUP():
    y = paddle_A.ycor()
    y = y+20
    paddle_A.sety(y)


def paddle_ADOWN():
    y = paddle_A.ycor()
    y = y-20
    paddle_A.sety(y)


def paddle_BUP():
    y = paddle_B.ycor()
    y = y+20
    paddle_B.sety(y)


def paddle_BDOWN():
    y = paddle_B.ycor()
    y = y-20
    paddle_B.sety(y)


def shapeshifter1():
    ball.color("red")


def shapeshifter2():
    ball.color("white")


pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A:0 player B:0", align="center",
          font=("Courier", 20, "normal"))

window.listen()
window.onkeypress(paddle_AUP, "w")
window.onkeypress(paddle_ADOWN, "s")
window.onkeypress(paddle_BUP, "Up")
window.onkeypress(paddle_BDOWN, "Down")

# Main loop
while start:
    window.update()
    gear = 2
    ball.setx(ball.xcor() + gear*ball.dx)
    ball.sety(ball.ycor() + gear*ball.dy)

    if ball.ycor() > height-10:
        ball.dy *= -1

    if ball.ycor() < -height+10:
        ball.dy *= -1

    if ball.xcor() > width-40:
        ball.goto(0, 0)
        scorea += 1
        ball.dx *= -1
        gear = 1

    if ball.xcor() < -width+40:
        ball.goto(0, 0)
        scoreb += 1
        ball.dx *= -1
        gear = 1

    pen.clear()
    pen.write("player A:{} player B:{}".format(scorea, scoreb), align="center",
              font=("Courier", 20, "normal"))

    if (ball.ycor() < paddle_A.ycor()+50 and ball.ycor() > paddle_A.ycor()-50) and (ball.xcor() < paddle_A.xcor()+20 and ball.xcor() > paddle_A.xcor()+10):
        ball.setx(paddle_A.xcor()+20)
        ball.dx *= -1

    if (ball.ycor() < paddle_B.ycor()+50 and ball.ycor() > paddle_B.ycor()-50) and (ball.xcor() > paddle_B.xcor()-20 and ball.xcor() < paddle_B.xcor()-10):
        ball.setx(paddle_B.xcor()-20)
        ball.dx *= -1
