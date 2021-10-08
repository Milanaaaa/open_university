for x in range(1, 200):
    a = 36 ** 17 - 6 ** x + 71
    s = ''
    while a > 0:
        s += str(a % 6)
        a = a // 6
    new = s[::-1]
    if sum([int(i) for i in new]) == 61:
        print(x, '!!!!!!!!!!!!!!!!')
    #print(x, sum([int(i) for i in new]))
