from ipaddress import ip_network

ip = ip_network('112.160.0.0/255.240.0.0')

cnt = 0
for i in ip:
    if f'{int(i):032b}'.count('1') % 5 == 0:
        cnt += 1
print(cnt)