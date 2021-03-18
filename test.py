# str = '1234567890'
# print(str[::-1])
# l = list(str)
# print(''.join(l))

# list1 = [1, 2]
# list2 = [3, 4]
# zip0 = zip(list1, list2)
# print(dict(zip(list1, list2)))


# def Fibonacci(loop):
#     if loop == 0:
#         return '无效参数'
#     elif loop == 1:
#         return 0
#     l = [0, 1]
#     for i in range(2, loop):
#         l.append(l[i - 1] + l[i - 2])
#     return l

# print(Fibonacci(3))


# li = [1, 2, 10, 4, 10, 4, 10, 2, 1]
#
# l = []
# for v in li:
#     if v == max(li):
#         l.append(v)
# print(l)
#
# print([v for v in li if v == max(li)])


# 水仙花
# list = []
# for i in range(100,1000):
#     a = i//100  # 百位上数字
#     b = (i-a*100)//10  # 十位上数字
#     c = i-a*100-b*10  # 个位上数字
#
#     # pow(x,y) 以x为底的y次方
#     if i == pow(a,3)+pow(b,3)+pow(c,3):
#         list.append(i)
# print(list)

# 完全数
# a = []
# for i in range(1, 1000):
#     sum = 0
#     for j in range(1,i):
#         if i % j == 0  and j < i:
#             sum = sum + j
#     if sum == i:
#         a.append(i)
# print(a)

# 幂的递归
# def mi(a, n):
#     if n == 0:
#         return 1
#     else:
#         return a * mi(a, n - 1)
# print(mi(3, 2))


# 目录遍历
import os


def get_file(path, rule=''):
    files = []
    for fpath, dirs, fs in os.walk(path):
        for f in fs:
            if os.path.join(fpath, f).endswith(rule):
                files.append(f)
    return files


# njoesnvefjon;vogf
