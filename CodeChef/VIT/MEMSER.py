for _ in range(int(input())):
    n = int(input())
    steps = list(input().split(' '))
    status = 0
    output = 200
    for i in range(n):
        if steps[i] == 'start' or steps[i] == 'restart':
            status = 1
        if steps[i] == 'stop':
            if(status == 0):
                output = 404
                break
            status = 0
    print(output)