n = 0
for a in 'rdl':
    for b in 'urdl':
        for c in 'urdl':
            for d in 'urdl':
                for e in 'urdl':
                    slovo = a + b + c + d + e
                    if slovo == slovo[::-1]:
                        n += 1
print(n)
