with open('input') as f:
    string = f.readline().strip()

# issue 1
# l = 4

# issue 2
l = 14 

for i in range(len(string) - l):
    if len(set(string[i : i + l])) == l:
        print(i + l)
        break
