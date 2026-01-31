def nto3(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n = n // 3
    return s
def R(n):
    s = nto3(n)
    if n % 3 == 0:
        s += s[-2:]  # дописываем две последние цифры
    else:
        sum_digits = sum(int(d) for d in s)
        add = nto3(sum_digits * 3)  # умножаем сумму на 3 и в троичную
        s += add
    return int(s, 3)
for N in range(1, 1000):
    r = R(N)
    if r > 208 and r % 2 == 1:
        print(r, N)
        #break
