l = int(input())
s = [char for char in input()]
# while((len(set(s[1::2]))!=len(s[1::2])) and len(s)%2==0):
c = 0
def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]
def perfect(s):
    if len(s)%2==0:
        a = [s[e:e+2] for e in range(0,len(s),2)]
        b = [unique(x) for x in a]
        if a!=b:
            return False
        else:
            return True
def clean(s):
    global c
    for x in range(0,l-1,2):
        if(s[x]==s[x+1]):
            s[x] = '_'
            c+=1
    s = [x for x in s if x!='_']
    if len(s)%2!=0 and len(s)!=1:
        c+=1
        s = s[:-1]
    if len(s)==1:
        c+=1
        s = []
    return s

while(not perfect(s)):
    s = clean(s)
print(c)
print(''.join(s))