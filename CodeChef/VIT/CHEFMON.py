from sys import stdin, stdout 
for _ in range(int(stdin.readline())):
    N, B = [int(x) for x in stdin.readline().split()] 
    nums = [int(x) for x in stdin.readline().split()] 
    max_sum = 0
    left, right = 0, 0
    curr_sum = nums[0]
    while (right < N and left < N):
        if (curr_sum <= B):
            max_sum = max(curr_sum, max_sum)
            right += 1
            curr_sum += nums[right] if right < N else 0

        else:
            curr_sum -= nums[left]
            left += 1
    stdout.write(str(max_sum))