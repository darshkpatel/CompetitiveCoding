from math import factorial,floor
def count_zeros(n):
    num = 5
    zeros = floor(n/num)
    total = zeros
    while(zeros!=0):
        num*=5
        zeros = floor(n/num)
        total+=zeros
    return total
cases = int(input())
for case in range(cases):
    num = int(input())
    print(count_zeros(num))

