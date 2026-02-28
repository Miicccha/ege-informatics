from itertools import product

cnt = 0
alph = '12345678'

for p in product(alph, repeat=9):
    s = ''.join(p)

    ok = True
    for i in range(8):
        if int(s[i]) % 2 == int(s[i+1]) % 2:
            ok = False
            break
    if not ok:
        continue

    good = True
    for d in alph:
        if s.count(d) > 3:
            good = False
            break

    if good:
        cnt += 1

print(cnt)