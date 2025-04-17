from ipaddress import ip_network

for mask in range(16, 25):
    ipp = ip_network(f'246.51.128.202/{mask}', False)
    for i in ipp:
        ip_2 = f'{int(i):032b}'
        if not(ip_2[:16].count('0') <= ip_2[16:].count('0')):
            break
    else:
        print(ipp.netmask)
        break

