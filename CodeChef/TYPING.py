for case in range(int(input())):
    time = 0
    words = []
    for test in range(int(input())):
        left = ['d', 'f']
        right= ['j', 'k']
        s = list(input(''))
        words.append(s)
        last = "l" if s[0] in left else "r"
        t_time = 2
        for x in range(1,len(s)):
            if s[x] in left and last == 'l':
                time+=2
                t_time+=2
                last = "l" if s[x] in left else "r"
            elif s[x] in left and last =='r':
                time+=4
                t_time += 4
                last = "l" if s[x] in left else "r"
            elif s[x] in right and last == "l":
                time+=4
                t_time += 4
                last = "l" if s[x] in left else "r"
            elif s[x] in right and last=='r':
                time+=2
                t_time += 2
                last = "l" if s[x] in left else "r"
        if s in words:
            time+=t_time/2
        else:
            time+-t_time
        print(s,t_time)

    print(time)

