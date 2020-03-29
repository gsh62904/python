#带圆点的七段数码管
import turtle as t
import time
def gap():
    t.penup()
    t.fd(6)   
def line(draw):#画一段线
    gap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    gap()
    t.right(90)
def dot():#画一个圆点
    t.pendown()
    t.begin_fill()
    t.color('green')
    t.circle(2,360)
    t.end_fill()
    t.penup()
def num(n):#画一个数字
    t.pendown()
    t.pencolor('red')
    line(True) if n in [2,3,4,5,6,8,9] else line(False) #第一笔
    line(True) if n in [0,1,3,4,5,6,7,8,9] else line(False)#第二笔
    line(True) if n in [0,2,3,5,6,8,9] else line(False)#第三笔
    line(True) if n in [0,2,6,8] else line(False)#第四笔
    t.left(90)
    line(True) if n in [0,4,5,6,8,9] else line(False)#第五笔
    line(True) if n in [0,2,3,5,6,7,8,9] else line(False)#第六笔
    line(True) if n in [0,1,2,3,4,7,8,9] else line(False)#第七笔
    t.right(180)
    t.penup()
    t.fd(20)
    dot()
    t.fd(20)
def date(date):#画一个串数字
    for i in date:
        num(eval(i))
              
def getdate():#获取系统年月日
    date = time.strftime('%Y%m%d',time.gmtime())
    return date
def main():
    t.setup(800,600)
    t.penup()
    t.fd(-360)
    t.pensize(5)
    t.pencolor("red")
    date(getdate())
    t.hideturtle()

main()

    
