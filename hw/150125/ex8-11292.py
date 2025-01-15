from itertools import product


cou = 0
for val in product('0123456789ABCDEF', repeat=5):
    if val.count('6') == 2 and val[0] != '0':
        if ('06' not in val) or ('26' not in val) \
            ('46' not in val) or ('66' not in val) \
            ('86' not in val) or ('A6' not in val) \
            ('C6' not in val) or ('E6' not in val):
            cou += 1
print(cou)

