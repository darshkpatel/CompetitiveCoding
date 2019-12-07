for case in range(int(input())):
    n = int(input())
    L = [x for x in range(1,n+1)]
    for i in range(n-1):
        L.append(L[0]+L[1]+L[0]*L[1])
        del L[1]
        del L[0]
    print(max(L))