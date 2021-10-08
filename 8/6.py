n = 0
for a in '0123':
    for b in '0123':
        for c in '0123':
            for d in '0123':
                slovo = a + b + c + d
                if slovo.count('0') >= 2 or slovo.count('1') >= 2 or slovo.count('2') >= 2 or slovo.count('3') >= 2:
                    n += 1
print(n)
