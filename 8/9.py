alf = {'0': 0,
       '1': 1,
       '2': 2,
       '3': 3,
       '4': 4,
       '5': 5,
       '6': 6,
       '7': 7,
       '8': 8,
       '9': 9,
       'a': 10,
       'b': 11,
       'c': 12,
       'd': 13,
       'e': 14,
       'f': 15
       }
cnt = 0
for n in range(1, 10000000):
    h = hex(n)[2:]
    ok = True
    for i in range(len(h) - 1):
        if (alf[h[i]] + alf[h[i + 1]]) % 2 == 0:
            ok = False
    if ok and len(h) ==4:
        #print(h)
        cnt+=1
print(cnt)
