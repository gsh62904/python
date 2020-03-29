#使用蒙特卡罗方法求圆周率
import random
random.seed(12)
dusts = 3000*3000
def jisuan():  
    hit = 0
    for i in range(dusts):
        x = random.random()
        y = random.random()
        if pow((x**2+y**2),0.5) < 1:
            hit +=1
    return hit
pi = 4*(jisuan()/dusts)
print(jisuan())
print('{0:.8f}'.format(pi))
