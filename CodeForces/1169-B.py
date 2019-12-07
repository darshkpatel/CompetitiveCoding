n,m = map(int, input().split(' '))
vals = []
output = "YES"
if m==1:
    print("YES")
    exit(0)
else:
    vals.append(list(map(int,input().split(' '))))
for x in range(1,m):
    new = list(map(int,input().split(' ')))
    if(len(set([vals[x-1][0],vals[x-1][1], new[0],new[1]]))==4):
        output="NO"
    vals.append(new)
print(output)