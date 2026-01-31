import string
alph='0123456789'+string.ascii_uppercase[:19]
for x in alph:
    s=int(f'923{x}874',29)+int(f'524{x}6152',29)
    if s%28==0:
        print(s//28)