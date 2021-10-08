a = 51 * 7 ** 12 - 7 ** 3 - 22
s = ''
while a > 0:
    s += str(a % 7)
    a = a // 7
new = s[::-1]
print(sum([int(i) for i in new]))
