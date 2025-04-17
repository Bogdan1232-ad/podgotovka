from ipaddress import ip_network

l = []
for i in range(9):
    l.append(int('1' * i + '0' * (8 - i), 2))


for a in l:
    ip = ip_network(f'152.65.245.132/255.255.{a}.0', False)
    for i in ip:
        if not (f'{int(i):032b}'[:16].count('0') >= f'{int(i):032b}'[16:].count('0')):
            break
    else:
        print(a)