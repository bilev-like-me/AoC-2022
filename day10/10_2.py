# issue 2
def print_screen(scr):
    print(''.join(scr[:40]))
    print(''.join(scr[40:80]))
    print(''.join(scr[80:120]))
    print(''.join(scr[120:160]))
    print(''.join(scr[160:200]))
    print(''.join(scr[200:240]))
    print()
    print()

def draw_pixel(c, v, s):
    vv = v + 40 * (c//40)
    if c in [vv, vv + 1, vv + 2]:
        s[c] = '#'

def new_pixel(c, v, s):
    draw_pixel(c, v, s)
    print_screen(s)

screen = ['.' for _ in range(240)]

print_screen(screen)
with open('input') as f:
    circle = 1
    value = 1
    new_pixel(circle, value, screen)
    while True:
        line = f.readline().strip()
        if line == '':
            break
        circle += 1
        new_pixel(circle, value, screen)
        if line.split()[0] == 'addx':
            circle += 1
            value += int(line.split()[1])
            new_pixel(circle, value, screen)
