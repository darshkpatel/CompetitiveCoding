def fact(n) :
    f = 1
    while n >= 1 :
        f = f * n
        n = n - 1
    return f
def findSmallerInRight(st, low, high) :

    countRight = 0
    i = low + 1
    while i <= high :
        if st[i] < st[low] :
            countRight = countRight + 1
        i = i + 1

    return countRight
def findRank (st) :
    ln = len(st)
    mul = fact(ln)
    rank = 1
    i = 0
    while i < ln :
        mul = mul / (ln - i)
        countRight = findSmallerInRight(st, i, ln- 1)
        rank = rank + countRight * mul
        i = i + 1
    return rank
def longest_prefix(a,b):
    length=0
    rang = len(a) if len(a)<len(b) else len(b)
    for i in range(rang):
        if(a[i]!=b[i]):
            break
        length+=1
    return length

chef_strings=[]
for x in xrange(int(raw_input(''))):
    chef_strings.append(raw_input(""))
for x in xrange(int(raw_input(''))):
    vars=raw_input("").split()
    r=int(vars[0])
    p=vars[1]
    chef_strings_split=chef_strings[:r]
    req_compare=[]
    max=0
    min_str=[]
    rank_min_str=9999999999999999999999999999999
    for string in chef_strings_split:
        lng=longest_prefix(string, p)
        if lng>max:
            max=lng
    for string in chef_strings_split:
        lng = longest_prefix(string, p)
        if lng==max:
            req_compare.append(string)
    for string in req_compare:
        rnk=findRank(string)
        if rnk==rank_min_str:
            min_str.append(string)
        elif rnk<rank_min_str:
            rank_min_str=rnk
            min_str.append(string)
    print min(min_str, key=len)

