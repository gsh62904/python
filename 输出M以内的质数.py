m = eval(input())
i=2
s = 0
for i in range(2,m+1):
    j = 2
    for j in range(2,i):
        if i % j ==0:
            break
    else:
        print(i)            

