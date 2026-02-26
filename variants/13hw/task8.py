import ipaddress

net = ipaddress.ip_network('120.91.176.213/255.255.192.0', False)

cnt=0
for ip in net:
    if bin(int(ip)):
        cnt+=1
print(cnt)
