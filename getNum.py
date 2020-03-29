def getNum():
    num = []
    numinput = input()
    while numinput != '':
        num.append(eval(numinput))
        numinput = input()
    return num
print(getNum())
