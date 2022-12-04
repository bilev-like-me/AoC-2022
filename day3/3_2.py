alp = [s for s in map(chr, range(ord('a'),ord('z')+1))] + [s for s in map(chr, range(ord('A'),ord('Z')+1))]
s = 0
with open('input') as f:
    while True:
        line1 = set(f.readline().strip())
        if line1 == set():
            break
        line2, line3 = set(f.readline().strip()), set(f.readline().strip())
        # print(line1, line2, line3)
        ss = (line3 - (line3 - (line1 - (line1 - line2))))
        # print(ss)
        s += alp.index(ss.pop()) + 1
print(s)
