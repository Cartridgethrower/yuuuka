#等位移凯撒密码
alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  #用alp定义了一个列表
s = input()
code = []                             #生成一个空列表
for i in range(len(s)):
    if 'A'<=s[i]<='Z' or 'a'<=s[i]<='z':
        c = s[i].upper()              #将小写英文字符换成大写，c是被大写后的s[i]
        k = alp.index(c)              #index函数，即55序列“ alp”中第一处出现字符c所代表的的英文的位置，而k值就是c在alp列表中的位置的值
        k = (k+i+1)%26                #等位移转换后新的位置，等号右边代码中，i是指在输入字符串中的位置，k是指在alp列表中的位置，由于是从0开始计算，所以要加1
        code.append(alp[k])           #appen函数，即在列表后加一个元素
    else:
        code.append(s[i])
print("".join(code))                  #join函数，可以将code列表中的元素都按原序连接起来，如果print的“”中有字符，则在每一个连接处加上这个字符
