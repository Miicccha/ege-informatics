import ipaddress

net = ipaddress.ip_network('122.159.136.144/255.255.255.248', False)

count = 0
for ip in net:
    if bin(int(ip)).count('1') %4 !=0:
        count +=1
print(count)