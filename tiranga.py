import turtle
t = turtle
t.penup()
t.backward(150)
t.left(90)
t.forward(100)
t.right(90)
t.pendown()
t.speed(100)
t.color("orange")
a=b=c=0

while a < 30 :
    t.forward(300)
    t.right(90)
    t.forward(1)
    t.right(90)
    t.forward(300)
    t.left(90)
    t.forward(1)
    t.left(90)
    a=a+1
t.color("white")
while b < 30 :
    t.forward(300)
    t.right(90)
    t.forward(1)
    t.right(90)
    t.forward(300)
    t.left(90)
    t.forward(1)
    t.left(90)
    b=b+1
t.color("green")
while c < 30 :
    t.forward(300)
    t.right(90)
    t.forward(1)
    t.right(90)
    t.forward(300)
    t.left(90)
    t.forward(1)
    t.left(90)
    c=c+1
    
t.penup()
t.color("blue")            
t.left(90)
t.forward(60)
t.right(90)
t.forward(150)
t.pendown()
t.circle(30)

t.left(90)
t.forward(60)

for i in range(0,10):
    t.right(110)
    t.circle(30,20)
    t.right(110)
    t.forward(60)

t.penup()
t.left(90)
t.circle(30,20)
t.left(180)
t.forward(150)
t.left(90)
t.forward(60)
t.left(90)
t.color("black")

t.exitonclick()