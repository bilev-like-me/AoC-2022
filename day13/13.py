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

# def extract_brackets(s):
#     lst = []
#     for i in range(len(s)):
#         if s[i] == '[':
#             lst.append((i,))
#         elif s[i] == ']':
#             for j in range(len(lst) - 1, -1, -1):
#                 if len(lst[j]) == 1:
#                     lst[j] += (i,)
#                     break
#     return lst

# def parce_lst_(s):
#     lst = s[1:-1].split(',')
#     print(lst)
#     input()
#     new_lst = []
#     for i in range(len(lst)):
#         print(lst[i])
#         if lst[i][0] == '[':
#             el = lst[i]
#             while True:
#                 i +=1
#                 if lst[i][-1] == ']':
#                     el += lst[i]
#                     new_lst.append(parce_lst(el))
#                     i += 1
#                     break
#                 else:
#                     el += lst[i]
#         else:
#             new_lst.append(int(lst[i]))
#     return lst

# with open('./day13/test_inp') as f:
with open('input') as f:
    cnt = 1
    total = 0
    while True:
        line1 = f.readline().strip()
        line2 = f.readline().strip()

        p1 = parce_lst(line1)
        p2 = parce_lst(line2)
        # print(p1[0])
        # print(p2[0])
        # print(compare_lst(p1[0], p2[0], 0))
        # input()
        total += cnt if compare_lst(p1[0], p2[0], 0) else 0

        line = f.readline()
        if line == '':
            break

        cnt += 1
    
    print(total)
