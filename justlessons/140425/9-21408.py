with open('9_21408.txt') as file:
    data = [list(map(int, i.split())) for i in file]

def f1(nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(3) == 6 and cnt.count(1) == 1

def f2(nums):
    maxx = 0
    nepov = 0
    for i in nums:
        if nums.count(i) > 1 and i > maxx:
            maxx = i
        if nums.count(i) == 1:
            nepov = i
    return maxx > nepov

cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1
print(cnt)