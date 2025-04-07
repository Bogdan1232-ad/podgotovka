with open('09_9778.txt') as file:
    data = [list(map(int, i.split())) for i in file]

def f1(nums):
    cnt = [nums.count(i) for i in nums]
    if cnt.count(2) == 2 and cnt.count(1) == 4:
        return True
    return False

def f2(nums):
    repeated = [i for i in nums if nums.count(i) == 2]
    aint = [i for i in nums if nums.count(i) == 1]
    return sum(aint) / len(aint) <= repeated[0]


for pos, i in enumerate(data):
    if f1(i) and f2(i):
        print(pos)
        break