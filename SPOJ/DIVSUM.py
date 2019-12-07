for case in xrange(int(raw_input(''))):
    num = int(raw_input('').strip())
    nsum=0
    for x in range(1,num):
        if num%x==0:
            nsum+=x
    print nsum