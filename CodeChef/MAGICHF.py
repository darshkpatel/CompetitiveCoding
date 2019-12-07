for case in range(int(input())):
    n,x,s = map(int, input().split(" "))
    current = x
    for swap in range(s):
        swp = list(map(int, input().split(" ")))
        if current in swp:
            if(swp[0]!=current):
                current=swp[0]
            else:
                current=swp[1]
    print(current)
