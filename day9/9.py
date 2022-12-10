def simulate(c):
    for i in range(30):
        print(i, end=' ')
        for j in range(30):
            for key, val in c.items():
                if [j - 15, 20 - i] == val:
                    print(key, end='')
                    break
            else:
                print('.', end='')
        print('')
    print('#'*40)
    input()

file = 'input'
# issue 1
distinct = {(0,0)}

c = {
    'H': [0, 0],
    'T': [0, 0]
}

with open(file) as f:
    for line in f:
        d, n = line.split()[0], int(line.split()[1])
        n = int(n)
        for _ in range(n):
            if d == 'R':
                c['H'][0] += 1
            elif d == 'L':
                c['H'][0] -= 1
            elif d == 'U':
                c['H'][1] += 1
            else:
                c['H'][1] -= 1
            for i in [0, 1]:
                a = c['H'][i] - c['T'][i]
                a = int((a/abs(a))*(abs(a)//2)) if a else 0
                if a:
                    c['T'][i] += a
                    c['T'][0 if i else 1] = c['H'][0 if i else 1]
                    break
            distinct.add(tuple(c['T']))

print('issue 1:', len(distinct))

# issue 2
distinct = {(0,0)}
c = {
    0: [0, 0], # 0 is H
    1: [0, 0],
    2: [0, 0],
    3: [0, 0],
    4: [0, 0],
    5: [0, 0],
    6: [0, 0],
    7: [0, 0],
    8: [0, 0],
    9: [0, 0]
}

with open(file) as f:
    for line in f:
        d, n = line.split()[0], int(line.split()[1])
        n = int(n)
        # simulate(c)
        for _ in range(n):
            if d == 'R':
                c[0][0] += 1
            elif d == 'L':
                c[0][0] -= 1
            elif d == 'U':
                c[0][1] += 1
            else:
                c[0][1] -= 1
            # simulate(c)
            for t in range(1, 10):
                for i in [0, 1]:
                    a = c[t - 1][i] - c[t][i]
                    a = int((a/abs(a))*(abs(a)//2)) if a else 0
                    if a:
                        c[t][i] += a
                        b = c[t - 1][0 if i else 1] - c[t][0 if i else 1]
                        if b == 0:
                            sign = 0
                        elif b > 0:
                            sign = 1
                        else:
                            sign = -1
                        c[t][0 if i else 1] += 1 * sign
                        break
                # simulate(c)
            distinct.add(tuple(c[9]))

print('issue 2:', len(distinct))
