"""
题目描述
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)，换行表示结束符，不算在字符里。不在范围内的不作统计。多个相同的字符只计算一次
输入
abaca
输出
3
输入描述:
输入N个字符，字符在ACSII码范围内。

输出描述:
输出范围在(0~127)字符的个数。

示例1
输入
abc
输出
3
"""
num = str(input())
ctr = 0
old = ''
for i in num:
    if 0 < ord(i) < 127 and i not in old:
        ctr += 1
        old += i
print(ctr)