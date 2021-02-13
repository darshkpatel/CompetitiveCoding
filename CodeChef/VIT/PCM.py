n = int(input())
for x in range(n):
    s = str(input()).strip()
    if('P' in s and 'C' in s and 'M' in s):
        print("YES")
    else:
        print("NO")