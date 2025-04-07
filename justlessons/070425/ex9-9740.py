from collections import Counter

with open('9_9740.txt') as file:
    data = [list(map(int, i.split())) for i in file]

def f1(nums):
    n = Counter(nums)
    return list(n.values()).count(1) == 4 and list(n.values()).count(3) == 3

def pov(nums):
    n = Counter(nums)
    l = []
    for i in nums:
        if n[i] == 3:
            return i


def f2(nums):
    nepov = [i for i in nums if nums.count(i) == 1]
    return sum(nepov) / len(nepov) <= pov(nums)

cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1
print(cnt)