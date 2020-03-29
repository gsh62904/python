def get():
    with open("hamlet.txt", "r") as f:
        txt = f.read()
        txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt
txt = get()
print(txt)
counts = {}    
words = txt.split()
print(words)
#for word in words:
#    counts[word] = counts.get(word,0) + 1
#items = list(counts.items())
#items.sort(key = lambda x:x[1],reverse = True)
#for i in range(10):
#    word,count = items[i]
#    print(word)
