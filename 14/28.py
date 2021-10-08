a = 2 ** 51 + 2 ** 40 + 2 ** 35 + 2 ** 17 - 2 ** 5
s = ''
while a > 0:
    s += str(a % 6)
    a = a // 6
new = s[::-1]
print(new.count('0')+new.count('1')+new.count('2')+new.count('3')+new.count('4')+new.count('5')+new.count('6')+new.count('7')+new.count('8')+new.count('9'))
