import ipaddress

net = ipaddress.ip_network('31.60.100.116/255.255.224.0', False) #131.32.255.131/255.255.240.0

cnt=0
for ip in net:
    if bin(int(ip)):
        cnt+=1
print(cnt)
