for i in range(int(input())):
    n,k = list(map(int,input().split(' ')))
    s = sorted(list(map(int,input().split(' '))))
    mdiff=max(s)-min(s)
    for i in range(n-k+1):
        diff=s[i+k-1]-s[i]
        mdiff=min(diff,mdiff)
    print(mdiff)
