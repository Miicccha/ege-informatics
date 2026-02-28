x=(2*16**2020+9*16**2021-2*4**2022+8**2023-2*2**2024-65536)
h=hex(x)[2:]
cnt=0
for c in h:
    if c in 'abcdef':
        cnt+=1
print(cnt)