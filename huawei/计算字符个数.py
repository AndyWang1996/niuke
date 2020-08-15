strs = input()
str1 = input()
strs = strs.lower()
str1 = str1.lower()
if str1 in strs:
    ctr = 0
    for i in strs:
        if i == str1:
            ctr += 1
        else:
            continue
    print(ctr)
else:
    print(0)