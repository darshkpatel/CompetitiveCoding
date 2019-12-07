def cnt(n):
    moves = 0
    if n==1:
        return 0
    if n==0:
        return -1
    else:
        while True:
            if n==1:
                return moves
            if n%5==0:
                n=n//5
                moves+=3
                continue
            if n%3==0:
                n=n//3
                moves+=2
                continue
            if n%2==0:
                n=n//2
                moves+=1
                continue
            else:
                if n!=1:
                    return -1
for case in range(int(input())):
    n = int(input())
    print(cnt(n))