n = 0
for a in '0246':
    for b in '01234567':
        for c in '01234567':
            for d in '01234567':
                slovo = a + b + c + d
                if sorted(slovo)[::-1] == list(slovo):
                    n += 1

print(n)
