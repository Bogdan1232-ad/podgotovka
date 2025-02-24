from fnmatch import fnmatch

for i in range(12345 - 12345 % 17, 10 ** 9, 17):
    if fnmatch(str(i), '1234*7'):
        print(i, i//141)
