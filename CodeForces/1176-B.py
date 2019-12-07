def count_threes(nums):
    total = 0
    old = len(nums)
    nums = list(filter(lambda a: a%3!=0, nums))
    total+=old-len(nums)
    ln = len(nums)
    nums = sorted(nums,reverse=True)
    for x in range(ln):
        for y in range(ln):
            if x!=y and nums[x]!=0 and nums[y]!=0 and (x+y)%3==0:
                total+=1
                nums[x]=0
                nums[y]=0
    nums = list(filter(lambda a: a!=0, nums))
    return(total)



for case in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split(' ')))
    nums = sorted(nums)
    print(count_threes(nums))
    
    
    
    