print('x y z w f')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = ((w or y) == x) or ((w <= z) and (y <= w))
                if not f:
                    print(x,y,z,w,f)

# x y z w f
# 0 0 0 1 False
# 0 1 0 0 False

# 0 1 0 1 False !1/3
# 0 0 0 1 False !2
# 0 1 1 0 False !1/3

#yxzw