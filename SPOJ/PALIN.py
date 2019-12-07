def ch_p(str):
    if str == str[::-1]:
        return True
    else:
        return False
def pali(n):
    if ch_p(n):
        n=list(n)
        if len(n)%2==0:



for case in xrange(int(raw_input(''))):
    a=list(raw_input('').strip())
    a[-1]=str(int(a[-1])+1)
    pali(a)