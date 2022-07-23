str1 = list(input())
str2 = list(input())
res = []
str1.sort()
str2.sort()

if str1 > str2:
    temp = str1
    str1 = str2
    str2 = str1

for i in range(len(str2)):
    res.append(chr(ord(str2[i])-1))

print(str1)
print(str2)
print(res)
