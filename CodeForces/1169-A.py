n,a,x,b,y = map(int,input().split(' '))

pos = [a,b]

while pos[0]!=x or pos[1]!=y:
    print(pos)
    if(pos[0]==pos[1]):
        print("YES")
        exit(0)
    if(pos[0]<n):
        pos[0]=pos[0]+1
    else:
        pos[0]=1
    if(pos[1]>1):
        pos[1]=pos[1]-1
    else:
        pos[1]=n
print("NO")
