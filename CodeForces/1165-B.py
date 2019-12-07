k = int(input())
p = sorted(list(map(int,input().split(' '))))
i=1
days = 0
while(days <= k):
    n = list(filter(lambda x: x >= i, p))
    if  len(n) > 0:
        p.remove(n[0])
        i+=1
        days+=1
    else:
        break
print(days)