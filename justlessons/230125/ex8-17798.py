from itertools import product

alph = sorted('МИНУС')
l = []
for pos, s in enumerate(product(alph, repeat=4), 1):
    s = ''.join(s)
    sogl = s.count('М') + s.count('Н') + s.count('С')
    gl = s.count("И") + s.count("У")
    if sogl >= gl:
        l.append(pos)

print(max(l))