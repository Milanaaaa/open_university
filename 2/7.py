print('a b c f')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f1 = b == ((a or c) <= b)
            if f1:
                print(a, b, c, f1)
print()

for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f2 = b == (a or (c <= b))
            if f2:
                print(a, b, c, f2)
# a b c f
# 0 1 0 1
# 1 0 0 1

# 0 1 1 1
# 1 1 0 1
# 1 0 1 1

# a b c f
# 0 0 1 True
# 0 1 0 True
# 1 0 0 True

# 0 1 1 True
# 1 0 1 True
# 1 1 0 True


