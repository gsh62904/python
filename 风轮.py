#自己编的
import turtle as t
t.pensize(2)
t.penup()
t.fd(150)
t.seth(90)
for i in range(4):
    t.penup()
    t.circle(150,45)
    t.pendown()
    t.circle(150,45)
t.left(90)
t.fd(300)
for i in range(3):
    t.penup()
    t.left(90)
    t.circle(150,45)
    t.pendown()
    t.left(90)
    t.fd(300)
t.goto(0,0)
#参考答案
import turtle as t
t.pensize(2)
for i in range(4):
    t.seth(90*i)
    t.fd(150)
    t.right(90)
    t.circle(-150, 45)
    t.goto(0,0)

    
  
