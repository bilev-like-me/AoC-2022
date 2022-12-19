# # issue 1
# def simulate_sand(w, md):
#     units = 0
#     while True:
#         x = 500
#         for deep in range(md + 1):
#             if x in w.keys():
#                 if deep + 1 in w[x]:
#                     if x - 1 not in w.keys():
#                         return units
#                     elif deep + 1 not in w[x - 1]:
#                         x = x - 1
#                     elif x + 1 not in w.keys():
#                         return units
#                     elif deep + 1 not in w[x + 1]:
#                         x = x + 1
#                     else:
#                         w[x].add(deep)
#                         units += 1
#                         break
#             else:
#                 return units
#         else:
#             return units

# issue 2
def simulate_sand(w, md):
    units = 0
    while True:
        x = 500
        if x in w.keys() and 0 in w[x]:
            return units
        for deep in range(md + 1):
            if x in w.keys():
                if deep + 1 in w[x]:
                    if x - 1 not in w.keys():
                        w[x - 1] = set([md + 1])
                        units += 1
                        break
                    elif deep + 1 not in w[x - 1]:
                        x = x - 1
                    elif x + 1 not in w.keys():
                        w[x + 1] = set([md + 1])
                        units += 1
                        break
                    elif deep + 1 not in w[x + 1]:
                        x = x + 1
                    else:
                        w[x].add(deep)
                        units += 1
                        break
            else:
                w[x] = set([md + 1])
                units += 1
                break
        else:
            if x in w.keys():
                w[x].add(md + 1)
            else:
                w[x] = set([md + 1])
            units += 1


walls = {}
max_deep = 0
with open('input') as f:
# with open('./day14/test_inp') as f:
    for line in f:
        wall = [tuple(map(int, x.split(','))) for x in line.strip().split('->')]
        for i in range(len(wall) - 1):
            if wall[i][0] == wall[i + 1][0]:
                a, b = wall[i][1], wall[i + 1][1]
                if a > b:
                    a, b = b, a
                if max_deep < b:
                    max_deep = b
                for dp in range(a, b + 1):
                    if wall[i][0] in walls.keys():
                        walls[wall[i][0]].add(dp)
                    else:
                        walls[wall[i][0]] = set([dp])
            else:
                if max_deep < wall[i][1]:
                    max_deep = wall[i][1]
                a, b = wall[i][0], wall[i + 1][0]
                if a > b:
                    a, b = b, a
                for wdt in range(a, b + 1):
                    if wdt in walls.keys():
                        walls[wdt].add(wall[i][1])
                    else:
                        walls[wdt] = set([wall[i][1]])

# for key in walls.keys():
#     print(key, walls[key])
# input()

print(simulate_sand(walls, max_deep))
