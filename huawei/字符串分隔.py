"""
题目描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述:
连续输入字符串(输入2次,每个字符串长度小于100)

输出描述:
输出到长度为8的新字符串数组
"""
while True:
    try:
        str1 = str(input())
        temp = ''
        for i in str1:
            temp += i
            if len(temp) == 8:
                print(temp)
                temp = ''
        if len(temp) is not 0:
            res = 8 - len(temp)
            for i in range(res):
                temp += '0'
            print(temp)
    except:
        break

