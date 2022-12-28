# issue 2

def append_diap(p, c):
    a, b, y = c[0], c[1], c[2]
    new_diap = []
    for e in p[y]:
        # print(f'{p[y]=}')
        # print(f'{e=} {a=} {b=}')
        if e[1] < a or e[0] > b:
            new_diap.append(e)
        elif e[0] == a:
            if e[1] > b:
                new_diap.append((b + 1, e[1]))
        elif e[0] < a and e[1] > a:
            new_diap.append((e[0], a - 1))
            if e[1] > b:
                new_diap.append((b + 1, e[1]))
        elif e[1] == a:
            if e[0] < e[1]:
                new_diap.append((e[0], a - 1))
        elif e[0] > a and e[1] > b:
            new_diap.append((b + 1, e[1]))
        # print(f'{new_diap=}')
        # print()
        # input()
    
    p[y] = new_diap

sens = []
max_f = 4000000
per = {x:[(0, max_f)] for x in range(max_f + 1)}
# print(per)
with open('input') as f:
    for line in f:
        line =  line.strip().replace(',', '=').replace(':', '=').split('=')
        sens.append(tuple([int(x) for x in [line[1], line[3], line[5], line[7]]]))

for s in sens:
    dist = abs(s[2] - s[0]) + abs(s[3] - s[1])
    offset = 0
    for y in range(s[1] - dist, s[1] + dist + 1):
        left = s[0] - offset
        right = s[0] + offset            
        if y >= 0 and y <= max_f:
            append_diap(per, (
                left if left >=0 else 0,
                right if right <= max_f else max_f,
                y
                ))
        offset += 1 if y < s[1] else -1
# for i in range(max_f):
#     if i in per.keys():
#         print(per[i])
#     else:
#         print('.' * max_f)
# print()
# print('#' * 40)
# print()
# input()

for k, v in per.items():
    if v:
        print(k + 4000000 * v[0][0])
        break


# # issue 1
# sens = []
# test = 2000000
# total = set()
# beacons = set()
# with open('input') as f:
#     for line in f:
#         line =  line.strip().replace(',', '=').replace(':', '=').split('=')
#         sens.append(tuple([int(x) for x in [line[1], line[3], line[5], line[7]]]))

# for s in sens:
#     if s[3] == test:
#         beacons.add(s[2])
#     dist = abs(s[2] - s[0]) + abs(s[3] - s[1])
#     if abs(test - s[1]) <= dist:
#         offset = (dist - abs(test - s[1])) * 2 + 1
#         total.update(set([x for x in range(s[0] - offset // 2, s[0] + offset // 2 + 1)]))

# # print(total)
# total.difference_update(beacons)
# print(len(total))
# # print(beacons)