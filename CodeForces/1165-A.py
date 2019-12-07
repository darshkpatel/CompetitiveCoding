n,x,y = map(int, input().split(' '))
num = str(input())[::-1]
changes = 0
i=0
while(i<y):
    # print(i)
    if(num[i]=='1'):
        # print("i={} 1 num[i]={}".format(i,num[i]))
        changes+=1
        i+=1
    else:
        i+=1
if(num[y]=='0'):
    # print(i)
    # print("i={} 2 num[i]={}".format(i,num[i]))
    changes+=1
i=y+1
while(i<x):
    # print(i)
    if(num[i]=='1'):
        changes+=1
        # print("i={} 3 num[i]={}".format(i,num[i]))
        i+=1
    else:
        i+=1
if(num[x]=='0'):
    # print(i)
    # print("i={} 4 num[i]={}".format(i,num[i]))
    changes+=1
print(changes)