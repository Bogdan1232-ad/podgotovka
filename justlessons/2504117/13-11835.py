from ipaddress import ip_network

cnt = 0
for i in range(256):
    net = ip_network(f'207.0.{i}.167/255.255.255.192', False)
    for j in net:
        j = f'{int(j):032b}'
        if not (j[:16].count('0') > j[16:].count('0')):
            break
    else:
        cnt += 1
print(cnt)