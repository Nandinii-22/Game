import turtle
import time
import time
import random

delay = 0.1


delay = 0.1

# Screen Setup

wn  = turtle.Screen()
wn.title("Snake Game by Nandini_Gupta")
wn.bgcolor("yellow")
wn.setup(width=600, height=600)
wn.tracer(0) # turns off the screen animation

 # Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake food
food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#Pen


# Functions
def go_up():
    if head.direction != "down":
       head.direction = "up"

def go_down():
     if head.direction != "up":
       head.direction = "down"
    
def go_right():
     if head.direction != "left":
        head.direction = "right"
    
def go_left():
     if head.direction != "right":
       head.direction = "left"    


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

# Keyboard bindings

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")


# Main Game loop
while True:
    wn.update()
       
    #check for collisions with wall
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        # Hide the segments
        for segment in segments:
            segment.goto(1000,1000)
        
        #Clear the segament list
        segments.clear()
           
    #Check for food collisions
    if head.distance(food)<20:
        #Moving food randomly
        x = random.randint(-290,290)
        y  = random.randint(-290,290)
        food.goto(x,y)
        
        # Adding segament
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)
        
 # Moving end segaments in reverse order    
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
        
    # Move segment 0 to head's position
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()
    time.sleep(delay)
    
wn.mainloop()