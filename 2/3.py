print('w y z x f')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (w or x or (not z) or y) and (w or x or (not z) or (not y)) and (w or (not x) or (not z) or (not y))

                if not f:
                    print(w, y, z, x, f)

#
# w y z x f
# 0 0 1 0 0
# 0 1 1 0 0
# 0 1 1 1 0