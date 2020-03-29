s = input()
t = ""
for c in s:
    if ord('a') <=ord(c) <= ord('w'): 
        t += chr( ord(c) + 3 )
    elif ord("x")<=ord(c)<=ord("z"):
        t+=chr(ord(c)-23)
    elif ord('A') <=ord(c) <= ord('W'):
         t += chr( ord(c) + 3 )
    elif ord('X') <=ord(c) <= ord('Z'):
        t+=chr(ord(c)-23)
    else:
        t += c
print(t)
