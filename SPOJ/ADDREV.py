
def rev(x):
    x = str(x)
    x = x.strip('0')
    return int(x[::-1])


for case in range(int(input())):
    a,b = map(int,input().split())
    addition = rev(a)+rev(b)
    print(rev(addition))