# 输入⼀个字符串，判断字符串中是否含有"ol"这个⼦串，若有把所有的"ol"替换为"fzu"，最后把字符串倒序输出
str_1 = input()
str_2 = []
flag = 0
for i in str_1:
    if flag == 0 and i == "o":
       flag = flag + 1
    elif flag == 1 and i == "l" :
        flag = 0
        str_2.append("f")
        str_2.append("z")
        str_2.append("u")
    elif flag == 1 and i != "l" :
        flag = 0
        str_2.append("o")
        str_2.append(i)
    else:
        str_2.append(i)
str_2.reverse()
print(''.join(str_2))
