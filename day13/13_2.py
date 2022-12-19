def parce_lst(s):
    lst = []
    num = ''
    i_iter = iter(range(1, len(s)))
    for i in i_iter:
        if s[i] == '[':
            pack = parce_lst(s[i:])
            lst.append(pack[0])
            for _ in range(pack[1]):
                next(i_iter)
        elif s[i] == ']':
            if num:
                lst.append(int(num))
            return [lst, i]
        elif s[i] == ',':
            if num:
                lst.append(int(num))
                num = ''
        else:
            num += s[i]

def compare_lst(l1, l2, deep):
    res = ''
    for el1, el2 in zip(l1, l2):
        if type(el1) is int and type(el2) is int:
            if el1 < el2:
                res = 'right'
            elif el1 > el2:
                res = 'not'
            else:
                pass
        elif type(el1) is list and type(el2) is list:
            res = compare_lst(el1, el2, deep + 1)
        elif type(el1) is list and type(el2) is int:
            res = compare_lst(el1, [el2], deep + 1)
        else:
            res = compare_lst([el1], el2, deep + 1)
        if res:
            if deep == 0:
                return True if res == 'right' else False
            else:
                return res
    
    if deep == 0:
        if len(l1) <= len(l2):
            return True
        else:
            return False
    else:
        if len(l1) < len(l2):
            return 'right'
        elif len(l1) > len(l2):
            return 'not'
        else:
            return ''

packets = []

with open('input') as f:
    while True:
        packets.append(parce_lst(f.readline().strip()))
        packets.append(parce_lst(f.readline().strip()))

        line = f.readline()
        if line == '':
            break

packets.append([[2]])
packets.append([[6]])

changed = True
while changed:
    changed = False
    for i in range(1, len(packets)):
        if compare_lst(packets[i], packets[i - 1], 0):
               packets[i - 1], packets[i] = packets[i], packets[i - 1]
               changed = True

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
