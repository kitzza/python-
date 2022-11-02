# 1 1 2 3
import sys

sys.setrecursionlimit(5000)  

from functools import lru_cache   # 极速递归


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)


for i in range(1,1000):
    print(i,f(i))