print('a b c f')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = (a and (not b)) or c
            print(a,b,c,f)
#a

# a b c f
# 0 0 0 0
# 0 0 1 1
# 0 1 0 0
# 0 1 1 1
# 1 0 0 1
# 1 0 1 1
# 1 1 0 0
# 1 1 1 1