print('x y z w f')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = ((x and (not y) or (w <= z)) == (z == x))
                if f:
                    print(x,y,z,w,f)
# x y z w f
# 0 1 0 0 True !2
# 1 0 1 0 True !1
# 1 0 1 1 True
# 1 1 0 1 True
# 1 1 1 0 True

#zywx