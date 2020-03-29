#斐波那契数列计算
def fbi(n):
    if n==1 or n==2:
        return 1
    elif n > 2:
        f = fbi(n-1) + fbi(n-2)
        return f
n = eval(input())
print(fbi(n))
