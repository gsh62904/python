import random
dusts=eval(input())
hits=0.0
random.seed(123)
for k in range(1,dusts+1):
    x = random.random()
    y = random.random()
    d = pow(x**2+y**2,0.5)
    if d <=1.0:
        hits = hits+1
pi=4*(hits/dusts)
print("{:.6f}".format(pi))

