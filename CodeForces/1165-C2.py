l = int(input())
s = [char for char in input()]
# while((len(set(s[1::2]))!=len(s[1::2])) and len(s)%2==0):
c = 0
def perfect(s):
    if len(s)%2==0 and all([1 for x in ])
def clean(s):
    global c
    for x in range(0,l-1,2):
        if(s[x]==s[x+1]):
            s[x] = '_'
            c+=1
    s = [x for x in s if x!='_']
    return s

print(clean(s))
if(len(s)%2!=0):
    c+=1
    del s[-1]
print(c)
print(''.join(s))