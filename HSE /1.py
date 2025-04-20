n = int(input())
a = list(map(int, input().split()))

if n % 2 != 0 or n == 0:
    print("No")
else:
    even_cnt = sum(1 for num in a if num % 2 == 0)
    if even_cnt % 2 == 0:
        print("Yes")
    else:
        print("No")