class Blizzards():
    def __init__(self, height, width, x, y, direction):
        self.h = height
        self.w = width
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        if self.direction == '>':
            self.x += 1
            if self.x == self.w - 1:
                self.x = 1
        elif self.direction == '<':
            self.x -= 1
            if self.x == 0:
                self.x = self.w - 2
        elif self.direction == '^':
            self.y -= 1
            if self.y == 0:
                self.y = self.h - 2
        else:
            self.y += 1
            if self.y == self.h - 1:
                self.y = 1


def print_field(b, h, w):
    for i in range(h):
        for j in range(w):
            dot = '.'
            if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                dot = '#'
            else:
                for el in b:
                    if el.x == j and el.y == i:
                        if dot == '.':
                            dot = el.direction
                        elif dot in ('>', '<', '^', 'v'):
                            dot = '2'
                        else:
                            dot = str(int(dot) + 1)
            print(dot, end='')
        print()
    print('-'*40)



# height = 0
# width = 0
bliz = []
with open('test_inp') as f:
    lines = []
    for line in f:
        lines.append(line.strip())
    height = len(lines)
    width = len(lines[0])
    lines = lines[1:-1]
    # print(f'{height=} {width=} {lines=}\n')
    for i in range(len(lines)):
        # print(f'{i=} {lines[i]}')
        bliz.extend([Blizzards(height, width, j, i + 1, d) for d, j in zip(lines[i], range(len(lines[i]))) if d != '#' and d != '.'])
        # print(f'{len(bliz)=} {[x.direction for x in bliz]=}')

# print(bliz)
for _ in range(1):
    print_field(bliz, height, width)
    for el in bliz:
        el.move()


queue = [(0, 1)] # (x-pos, y-poz) for every element in queue
minute = 1
bingo = False
while queue:
    if minute % 5 == 0:
        print(f'{minute=} {len(queue)=}')
    new_queue = []
    minute += 1
    for b in bliz:
        b.move()
    for el in queue:
        # print([el, (el[0] - 1, el[1]), (el[0] + 1, el[1]), (el[0], el[1] - 1), (el[0], el[1] + 1)])
        # input()
        for np in [el, (el[0] - 1, el[1]), (el[0] + 1, el[1]), (el[0], el[1] - 1), (el[0], el[1] + 1)]:
            if np == (height - 1, width - 2):
                print(minute)
                bingo = True
                break
            elif np[0] > 0 and np[0] < height - 1 and np[1] > 0 and np[1] < width - 1:
                for b in bliz:
                    if (b.x, b.y) == np:
                        break
                else:
                    if np not in new_queue:
                        new_queue.append(np)
        if bingo:
            queue = []
            break
    if not bingo:
        queue = new_queue
