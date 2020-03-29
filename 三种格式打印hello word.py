s = input()
if eval(s) == 0:
    print("Hello World")#直接不换行输出''
elif eval(s) > 0 :
    print("He""\nll""\no ""\nWo""\nrl""\nd")#每两个字符换行输出
else:
    for c in str('Hello World'):#遍历字符串，每个字符换行一次输出
        print(c)
        
b= 'Hello World'
for n in range(len(b)):#遍历字符串长度，并将每个字符位置打印一次
    print(b[n])
   
