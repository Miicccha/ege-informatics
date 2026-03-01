import ipaddress
net = ipaddress.ip_network('191.128.66.83/255.192.0.0', False)
print(net.broadcast_address)