c=[]
for i in range(100,1000):
    a =str(i)
    if i==pow(eval(a[0]),3)+pow(eval(a[1]),3)+pow(eval(a[2]),3):
        c.append(i)
print(str(c)[1:-1])


            

s = ""
for j in range(100, 1000):
    t = str(j)
    if pow(eval(t[0]),3) + pow(eval(t[1]),3) + pow(eval(t[2]),3) == j :
        s=s+'{},'.format(str(j))
print(s[:-1])
print("{},"[:-1].format(j))
