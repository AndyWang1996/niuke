"""
题目描述
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。

输入描述:
 输入一个整数（int类型）

输出描述:
 这个数转换成2进制后，输出1的个数

示例1
输入
5
输出
2
"""
num = int(input())
ctr = 0
while num is not 0:
    if num%2 == 1:
        num = num/2
        ctr += 1
    else:
        num = num/2
    num = int(num)
print(ctr)