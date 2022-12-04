alp = [s for s in map(chr, range(ord('a'),ord('z')+1))] + [s for s in map(chr, range(ord('A'),ord('Z')+1))]
s = 0
with open('input') as f:
    for line in f:
        line = line.strip()
        a, b = set(line[:len(line)//2]), set(line[len(line)//2:])
        s += alp.index((a - (a - b)).pop()) + 1
print(s)
