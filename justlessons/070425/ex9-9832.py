with open('9_9832.txt') as file:
    data = [list(map(int, i.split())) for i in file]

def f1(nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(2) == 4 and cnt.count(1) == 3

def f2(nums):
    nums = sorted(nums)
    return nums[6] not in nums[:6]

for i in data:
    if f1(i) and f2(i):
        print(sum(i))
        break