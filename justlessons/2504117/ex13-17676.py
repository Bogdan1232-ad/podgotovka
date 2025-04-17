from ipaddress import ip_network

ip = ip_network('115.192.0.0/255.192.0.0')

cnt = 0
for i in ip:
    if f'{int(i):032b}'.count('1') % 3 != 0:
        cnt += 1

print(cnt)