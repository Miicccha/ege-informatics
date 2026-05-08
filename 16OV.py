from functools import lru_cache
import sys 
sys.setrecursionlimit(3000000)
sys.set_int_max_str_digits(0)

@lru_cache(None)
def F(n):
    if n<10:
        return 1
    else:
        return(n+3)*F(n-3)
for i in range(0,250000):
    F(i)
print(F(247563)/(519-477*F(247560)/F(247557)))