def parce_lst(s):
    lst = []
    num = ''
    for el, i in zip(s[1:],range(len(s) - 1)):
        if el == '[':
            pack = parce_lst(s[i + 1:])
            lst.append(pack[0])
            i += pack[1]
        elif el == ']':
            if num:
                lst.append(int(num))
            return [lst, i + 1]
        elif el == ',':
            lst.append(int(num))
            num = ''
        else:
            num += el

def extract_brackets(s):
    lst = []
    for i in range(len(s)):
        if s[i] == '[':
            lst.append((i,))
        elif s[i] == ']':
            for j in range(len(lst) - 1, -1, -1):
                if len(lst[j]) == 1:
                    lst[j] += (i,)
                    break
    return lst

def parce_lst_(s):
    lst = s[1:-1].split(',')
    print(lst)
    input()
    new_lst = []
    for i in range(len(lst)):
        print(lst[i])
        if lst[i][0] == '[':
            el = lst[i]
            while True:
                i +=1
                if lst[i][-1] == ']':
                    el += lst[i]
                    new_lst.append(parce_lst(el))
                    i += 1
                    break
                else:
                    el += lst[i]
        else:
            new_lst.append(int(lst[i]))
    return lst

with open('./day13/test_inp') as f:
    while True:
        line1 = f.readline().strip()
        line2 = f.readline().strip()

        # b1 = extract_brackets(line1)
        # b2 = extract_brackets(line2)
        print(parce_lst(line1))
        print(parce_lst(line2))
        input()





        line = f.readline()
        if line == '':
            break
