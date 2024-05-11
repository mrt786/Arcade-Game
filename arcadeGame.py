from turtle import Turtle, Screen

screen = Screen()
screen.title("Arcade Game")
screen.setup(width=800 , height=600)
width = 800
height = 600
screen.bgcolor("grey")
left_paddle = Turtle()
left_paddle.penup()
left_paddle.setheading(90)
left_paddle.shape(name="square")
left_paddle.color("red")
left_paddle.shapesize(1,6)
left_paddle.goto((width/2)*-1,0)#appear on the left side of the screen 
 
right_paddle = Turtle()
right_paddle.penup()
right_paddle.setheading(90)
right_paddle.shape(name="square")
right_paddle.color("blue")
right_paddle.shapesize(1,6)
right_paddle.goto((width/2)*1-7,0) 
scale_factor_paddle_2 = -7#to  appear on right side of the screen a

ball = Turtle()
def make_ball():
    global ball
    ball.penup()
    ball.setheading(90)
    ball.shape(name="circle")
    ball.color("orange")

make_ball()
def move_right_paddle(key):
    global right_paddle,right_paddle_y
    right_paddle_y = right_paddle.ycor()
    if key =="Up":
        if right_paddle_y < 240:
            right_paddle.forward(15)
    else:
        if(right_paddle_y > -230):
            right_paddle.backward(15) 
def move_left_paddle(key):
    global left_paddle ,left_paddle_y
    left_paddle_y = left_paddle.ycor()
    if key =="w":
        if left_paddle_y < 240:
            left_paddle.forward(15)
    else:
        if(left_paddle_y > -230):
            left_paddle.backward(15) 
def move_ball(event):
    global ball, x, y,direction,least_count
    if (event == "right" and direction == "up"):#the ball will move in the first quad
        x+=2
        y+=2
    elif (event == "right" and direction == "down"):#the ball will move in the 4th quad
        x+=2
        y-=2
    elif (event == "left" and direction == "up"):# the ball willl move in the 2nd quad
        x-=2
        y+=2
    elif (event == "left" and direction == "down"):# the ball will move in the third quad
        x-=2
        y-=2  
    least_count+=2
    if least_count == 10 or y%10==0:
        least_count = 0
def wall_collision():
    global ball, x, y,event,direction
    if y>=height/2 and (event =="left" or event == "right"):
        direction = "down"
    elif y < (-(height/2)) and (event == "right" or event == "left") and direction =="down":
        direction = "up"
def paddle_collision():
    global left_paddle_x,left_paddle_y,left_paddle_y,left_paddle_y,x,y,direction,event,least_count
    # if y>0:
    #     least_count*=1   
    # else:#  when the y cordiante is negative the the least count will added
    #     least_count*=-1
    if left_paddle_x ==x and (left_paddle_y +60== y-least_count or  y-least_count== left_paddle_y-60):# if collison is with edge of the paddle
        ball.color("blue")
        event = "right"
        if direction == "up":
            direction = "down"
        else:
            direction = "up"
    elif left_paddle_x ==x and left_paddle_y +80 > y > left_paddle_y-80:
        ball.color("red")
        event= "right"
    if right_paddle_x < x and (right_paddle_y + 60 == y-least_count or right_paddle_y -60 ==y - least_count ):
        
        if direction == "up":
            direction = "down"
        else:
            direction = "up"
        event = "left"
        ball.color("red")
    elif right_paddle_x< x and (right_paddle_y +80) >y > (right_paddle_y-80):
        ball.color("blue")
        event = "left"
screen.listen()
event_array = ["right" , "left"]
direction_array = ["up" , "down"]
import random
event = random.choice(event_array)
direction = random.choice(direction_array)
x = ball.xcor()
y = ball.ycor()
least_count = 0
# The x and y cordiante of the left paddle
left_paddle_x = left_paddle.xcor()
left_paddle_y = left_paddle.ycor()
# The x and y cordiante of the right paddle
right_paddle_x = right_paddle.xcor()
right_paddle_y = right_paddle.ycor()
check = True
while check:
    for key in ["Up" , "Down"]:
        screen.onkey(lambda k=key: move_right_paddle(k), key)
    for key in ["w" , "s"]:
        screen.onkey(lambda k=key: move_left_paddle(k), key)
    move_ball(event)
    wall_collision()
    paddle_collision()
    if y> (-height/2):
        wall_collision()
    ball.goto(x ,y)
    if x>width/2 or x<-(width/2)-8:
        check = False
        ball.hideturtle()
        ball.goto(0,0)
        left_paddle.hideturtle()
        right_paddle.hideturtle()
        ball.hideturtle()
        ball.write("Game Over",align ="center",font = ("Arial" ,"24" ,"normal"))
        
screen.exitonclick()