print('a b c d f')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f = ((a == b) or (not (c == d)) and (b <= (not c)))
                if not f:
                    print(a, b, c, d, f)

# a b c d f
# 0 1 0 0 False
# 0 1 1 0 False
# 1 0 0 0 False
#dacb