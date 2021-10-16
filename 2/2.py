print('y w z x f')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = w and (x == (z<=y))
            if f:
                print(y,w,z,x, f)
# y w z x
