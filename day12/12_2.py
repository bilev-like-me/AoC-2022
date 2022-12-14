
field = []
with open('input') as f:
    for line in f:
        field.append(line.strip())

for i in range(len(field)):
    if 'S' in field[i]:
        xs = field[i].find('S')
        ys = i
        break

ays = [(xs, ys)]
height = len(field)
width = len(field[0])

for y in range(height):
    for x in range(width):
        if field[y][x] == 'a':
            ays.append((x, y))

best_f = 2**350 + 1
for a in ays:
    field[a[1]] = field[a[1]][:a[0]] + 'S' + field[a[1]][a[0] + 1:]
    way = [[99999 for _ in range(width)] for __ in range(height)]
    check = [(a[0], a[1])]
    way[a[1]][a[0]] = 0
    fewest = 2**350
    # for el in field:
    #     print(el)
    while check:
        # for el in way:
        #     print(el)
        # input()
        new_check = []
        for p in check:
            if p[0] - 1 >= 0:
                cost1 = ord(field[p[1]][p[0] - 1]) if field[p[1]][p[0] - 1] != 'E' else ord('z')
                cost2 = ord(field[p[1]][p[0]]) if field[p[1]][p[0]] != 'S' else ord('a')
                if cost1 - cost2 < 2 and way[p[1]][p[0] - 1] > way[p[1]][p[0]] + 1:
                    way[p[1]][p[0] - 1] = way[p[1]][p[0]] + 1
                    new_check.append((p[0] - 1, p[1]))
                    if field[p[1]][p[0] - 1] == 'E':
                        if fewest > way[p[1]][p[0] - 1]:
                            fewest = way[p[1]][p[0] - 1]
            if p[0] + 1 < width:
                cost1 = ord(field[p[1]][p[0] + 1]) if field[p[1]][p[0] + 1] != 'E' else ord('z')
                cost2 = ord(field[p[1]][p[0]]) if field[p[1]][p[0]] != 'S' else ord('a')
                if cost1 - cost2 < 2 and way[p[1]][p[0] + 1] > way[p[1]][p[0]] + 1:
                    way[p[1]][p[0] + 1] = way[p[1]][p[0]] + 1
                    new_check.append((p[0] + 1, p[1]))
                    if field[p[1]][p[0] + 1] == 'E':
                        if fewest > way[p[1]][p[0] + 1]:
                            fewest = way[p[1]][p[0] + 1]
            if p[1] - 1 >= 0:
                cost1 = ord(field[p[1] - 1][p[0]]) if field[p[1] - 1][p[0]] != 'E' else ord('z')
                cost2 = ord(field[p[1]][p[0]]) if field[p[1]][p[0]] != 'S' else ord('a')
                if cost1 - cost2 < 2 and way[p[1] - 1][p[0]] > way[p[1]][p[0]] + 1:
                    way[p[1] - 1][p[0]] = way[p[1]][p[0]] + 1
                    new_check.append((p[0], p[1] - 1))
                    if field[p[1] - 1][p[0]] == 'E':
                        if fewest > way[p[1] - 1][p[0]]:
                            fewest = way[p[1] - 1][p[0]]
            if p[1] + 1 < height:
                cost1 = ord(field[p[1] + 1][p[0]]) if field[p[1] + 1][p[0]] != 'E' else ord('z')
                cost2 = ord(field[p[1]][p[0]]) if field[p[1]][p[0]] != 'S' else ord('a')
                if cost1 - cost2 < 2 and way[p[1] + 1][p[0]] > way[p[1]][p[0]] + 1:
                    way[p[1] + 1][p[0]] = way[p[1]][p[0]] + 1
                    new_check.append((p[0], p[1] + 1))
                    if field[p[1] + 1][p[0]] == 'E':
                        if fewest > way[p[1] + 1][p[0]]:
                            fewest = way[p[1] + 1][p[0]]
        check = new_check.copy()
    if fewest < best_f:
        best_f = fewest
    
    field[a[1]] = field[a[1]][:a[0]] + 'a' + field[a[1]][a[0] + 1:]

print(best_f)
