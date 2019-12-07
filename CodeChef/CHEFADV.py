for case in range(int(input())):
    n,m,x,y = map(int,list(input().split(' ')))
    if n!=x:
        n-=1
    if m!=y:
        m-=1
    if((n%x==0 and m%y==0) or (n%x==1 and m%y==1) or (n>=2 and n%x==1 and y==1) or (m>=2 and m%y==1 and x==1)):
        print("Chefirnemo")
    else:
        print("Pofik")