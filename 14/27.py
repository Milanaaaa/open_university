a = 7 * 1296 ** 57 - 8 * 216 ** 30 + 35
s = ''
while a > 0:
    s += str(a % 6)
    a = a // 6
new = s[::-1]
print(new.count('5'))
