t_score = 0
elf = 'ABC'
iam = 'XYZ'

# with open('test_inp') as f:
with open('input') as f:
    total = 0
    for line in f:
        a, b = int(iam.index(line.strip()[2])), int(elf.index(line.strip()[0]))
        rez = a + 1
        if a - b == 0:
            rez += 3
        elif a - b in (-2, 1):
            rez += 6
        else:
            pass
        # print(rez)
        total += rez
    print(total)
