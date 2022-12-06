with open('input') as f:
    line = f.readline()
    cr_cnt = len(line) // 4
    cranes = {x:[] for x in range(1, cr_cnt + 1)}
    while line[1] != '1':
        for key in range(1, cr_cnt + 1):
            el = line[key * 4 - 3]
            if el != ' ':
                cranes[key].append(el)
        line = f.readline()
    f.readline()
    height = len(cranes[1])
    while True:
        line = f.readline()
        if line.strip() == '':
            break
        move = [int(line.split()[x]) for x in (1, 3, 5)]
        
        # # issue 1
        # for _ in range(move[0]):
        #     cranes[move[2]] = [cranes[move[1]][0]] + cranes[move[2]]
        #     cranes[move[1]] = cranes[move[1]][1:]
        
        # issue 2
        cranes[move[2]] = cranes[move[1]][:move[0]] + cranes[move[2]]
        cranes[move[1]] = cranes[move[1]][move[0]:]

    print(''.join([cranes[x + 1][0] for x in range(cr_cnt)]))            
