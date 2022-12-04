cals = []
with open('inp') as file:
    cal = 0
    for line in file:
        if line.strip() == '':
            cals.append(cal)
            cal = 0
        else:
            cal += int(line.strip())


cals.sort()
print(f'1 issue: {cals[-1]}')
print(f'2 issue: {sum(cals[-3:])}')
