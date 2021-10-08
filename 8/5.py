n = 0
for a in '01234567':
    for b in '0246':
        for c in '1357':
            for d in '0246':
                for e in '01234567':
                    if len(set(a+b+c+d+e)) == 5:
                        n += 1
print(n)