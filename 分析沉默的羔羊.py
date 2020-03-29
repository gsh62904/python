import jieba
sources = open('sheep.txt','r',encoding = 'utf-8')
stxt = sources.read()
words = jieba.lcut(stxt)
excep_t = {'什么','没有','他们','我们','一个','知道','可以','东西','自己','医生',
           '就是','可能','已经','还是','一下','这个','这儿','先生','现在','看到',
           '一只','出来','这么','事儿'}
counts = {}
for word in words:
    if len(word) ==1 or word in excep_t:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key = lambda x:x[1],reverse = True)
for i in range(10):
    key,value = items[i]
    print(key,value)
    
    
    
