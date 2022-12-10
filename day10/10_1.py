# issue 1
points = [20, 60, 100, 140, 180, 220]
with open('input') as f:
    circle = 1
    value = 1
    power = 0
    while True:
        line = f.readline()
        if line.strip() == '':
            break
        if line.split()[0] == 'noop':
            circle +=1
            if circle == points[0]:
                power += value * points[0]
                points = points[1:]
        else:
            circle +=2
            if circle == points[0]:
                value += int(line.split()[1])
                power += value * points[0]
                points = points[1:]
            elif circle == points[0] + 1:
                power += value * points[0]
                points = points[1:]
                value += int(line.split()[1])
            else:
                value += int(line.split()[1])
        if circle >= 220:
            break

print(power)
