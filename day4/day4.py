with open('input') as f:
    s = 0
    s2 = 0
    while True:
        line = f.readline().strip()
        if line == '':
            break

        a, b = (set([y for y in range(int(x.split('-')[0]), int(x.split('-')[1]) + 1)]) for x in line.split(','))
        # day 4 issue 1
        s += 1 if a.issubset(b) or b.issubset(a) else 0
        # day 4 issue 2
        s2 += 1 if a & b else 0

    print(f'1 issue: {s}\n2 issue: {s2}')
