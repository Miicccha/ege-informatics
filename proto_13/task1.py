import ipaddress
arr=[]
for i in range(1, 255):
    cnt =0
    net = ipaddress.ip_network(f'122.159.136.144/{i}', False)
    for ip in net:
        cnt +=1
        print(bin(int(ip))[2:],cnt,i)
    arr.append(cnt)
print(min(arr))