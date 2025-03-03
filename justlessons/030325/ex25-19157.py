from itertools import product

for que in '0123456789':
    for i in range(4):
        for star in product('0123456789', repeat=i):
            for j in range(4):
                for star2 in range('0213456789', repeat=i):
                    s = '1' + que + '3' + star + '5' + star2 + '954'
                    s = int(s)
                    if s < 10 ** 10:
                        pass