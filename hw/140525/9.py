with open('9_5489.txt') as file:
	data = [list(map(int, i.split())) for i in file]

def f1(nums):
	return len(set(nums)) == len(nums) 

def f23(nums):
	chet = [i for i in nums if i % 2 == 0]
	nechet = [i for i in nums if i % 2 == 1]
	return len(chet) > len(nechet) and sum(chet) < sum(nechet)

cnt = 0
for i in data:
	if f1(i) and f23(i):
		cnt += 1

print(cnt)