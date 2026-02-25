import ipaddress

net = ipaddress.ip_network('192.158.32.160/255.255.255.224', False)

count = 0
for ip in net:
    if bin(int(ip)):
        count +=1
        #print(ip)
print(count%2)