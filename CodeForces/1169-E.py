n,q = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
for x in range(q):
    x,y = map(int, input().split(' '))
    if (x<y) and ((a[x-1]&a[y-1])>0):
        print("Shi")
    else:
        print("Fou")

