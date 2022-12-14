def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(int(n))
    p_dickt = {}
    for el in set(primfac):
        p_dickt[el] = primfac.count(el)
    p_dickt['sum'] = 0
    return p_dickt

total = 0

M = {}
with open('test_inp') as f:
    while True:
        monkey = int(f.readline().strip().strip(':').split()[1])
        items = [primfacs(y) for y in [int(x.strip(',')) for x in f.readline().split()[2:]]]
        operation = f.readline().split()[-3:]
        test = [int(f.readline().split()[-1]), int(f.readline().split()[-1]), int(f.readline().split()[-1])]

        M[monkey] = {'i':items, 'o': operation, 't': test, 'c': 0} 

        line = f.readline()
        if line == '':
            break
for i in range(len(M)):
    print(M[i])
input()
# r = 20 # for issue 1
r = 10000 # for issue 2

for round in range(1, r + 1):
    for m in range(len(M)):
        while True:
            if M[m]['i'] == []:
                break
            else:
                M[m]['c'] += 1

            item = M[m]['i'].pop(0)            
            # op1 = item if M[m]['o'][0] == 'old' else int(M[m]['o'][0])
            # op2 = item if M[m]['o'][2] == 'old' else int(M[m]['o'][2])
            # print(f'Calculating on round: {round} ...')
            if M[m]['o'][1] == '+':
                total += int(M[m]['o'][2])
                print(round, item['sum'], end=' >>> ')
                item['sum'] += int(M[m]['o'][2])
                print(item['sum'])
                input()
            else:
                op2 = item if M[m]['o'][2] == 'old' else primfacs(int(M[m]['o'][2]))
                for key in op2.keys():
                    if key in item.keys():
                        item[key] += op2[key]
                    else:
                        item[key] = op2[key]

            if  M[m]['t'][0] in item.keys() and item['sum'] % M[m]['t'][0] == 0:
                M[M[m]['t'][1]]['i'].append(item)
            else:
                # print(M[m]['t'][0], item)
                # input()
                M[M[m]['t'][2]]['i'].append(item)

            # next line commented for issue 2
            # ans = ans//3
            # for key in range(len(M)):
            #     print(key, ':', M[key])

            # if ans == M[m]['t'][0] * (ans//M[m]['t'][0]):
            # print(f'Check devising on round: {round} ...')
            # if ans % M[m]['t'][0] == 0:
            #     M[M[m]['t'][1]]['i'].append(ans // M[m]['t'][0])
            # else:
            #     M[M[m]['t'][2]]['i'].append(ans)

    if round in (1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000):
        print(round, [f"{M[x]['c']} {M[x]['i']}" for x in range(len(M))])
        
# print(M)
score = [M[x]['c'] for x in range(len(M))]
score.sort()
print(score[-1] * score[-2])
print(f'{total=}')
