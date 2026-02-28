import ipaddress

net = ipaddress.ip_network('116.192.155.16/255.255.255.0', False)

cnt = 0
for ip in net:
    b = bin(int(ip))[2:]
    if b[-2:]=='00' or b[-2:]=='11':
        cnt +=1
print(cnt,)