#等位移凯撒密码解码
alp = "abcdefghijklmnopqrstuvwxyz"
s = input()
code = []
for i in range(len(s)):
    if 'A'<=s[i]<='Z' or 'a'<=s[i]<='z':
        c = s[i].lower()
        k = alp.index(c)
        k = (k-i-1)%26
        code.append(alp[k])
    else:
        code.append(s[i])
print("".join(code))
