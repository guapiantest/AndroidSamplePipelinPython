# 幂的递归
def mi(a, n):
    if n == 0:
        return 1
    else:
        return a * mi(a, n - 1)


print(mi(3, 2))
