def get_size(tree, dir):
    sum = 0
    for el in tree[dir]:
        if type(el) is int:
            sum += el
        else:
            sum += get_size(tree, el)
    return sum

needToRead = True
eof = False
tree = {}
cur_dir = []
with open('input') as f:
    while True:
        if eof:
            break
        if needToRead:
            line = f.readline().strip().split()
        needToRead = True
        if line == []:
            break
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '..':
                    cur_dir = cur_dir[:-1] 
                else:
                    cur_dir.append(line[2])
                    if '.'.join(cur_dir) not in tree.keys():
                        tree['.'.join(cur_dir)] = []
            elif line[1] == 'ls':
                while True:
                    line = f.readline().strip().split()
                    if line == []:
                        eof = True
                        break
                    elif line[0] == '$':
                        needToRead = False
                        break
                    elif line[0] == 'dir':
                        tree['.'.join(cur_dir)].append('.'.join(cur_dir) + '.' + line[1])
                    else:
                        tree['.'.join(cur_dir)].append(int(line[0]))

# print(tree)
# issue 1
# total = 0
# for dir in tree.keys():
#     size = get_size(tree, dir) 
#     if size <= 100000:
#         total += size

# print(total)

#issue 2
dir_to_delete = get_size(tree, '/')
space_needed = dir_to_delete - 40000000
for dir in tree.keys():
    size = get_size(tree, dir)
    if size >= space_needed and size < dir_to_delete:
        dir_to_delete = size

print(dir_to_delete)

