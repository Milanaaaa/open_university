print('a b c d f')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f = a == d or c and (not b)
                print(a, b, c, d, f)