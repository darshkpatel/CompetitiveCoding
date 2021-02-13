for _ in range(int(input())):
    N=int(input())
    height=list(map(int,input().split(' ')))
    iq=list(map(int,input().split(' ')))
    memo=[1]*(N+1)
    for i in range(1,N):
        for j in range(i):
            if height[i]>height[j] and iq[i]<iq[j]:
                memo[i]=max(memo[i],memo[j]+1)
    
    print(max(memo))