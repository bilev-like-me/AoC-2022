def snafu_dec(sn):
    power = 0
    dec = 0
    for el in sn[::-1]:
        if el == '-':
            el = -1
        elif el == '=':
            el = -2
        dec += int(el) * (5 ** power)
        power += 1
    return dec

def dec_snafu(num):
    sn = ''
    mem = 0
    while num:
        offset = num % 5
        if offset + mem in (0, 1, 2):
            sn = str(offset + mem) + sn
            mem = 0
        elif offset + mem == 3:
            sn = '=' + sn
            mem = 1
        elif offset + mem == 4:
            sn = '-' + sn
            mem = 1
        else:
            sn = '0' + sn
            mem = 1
        num = num // 5
    return sn


total = 0
with open('input') as f:
    for line in f:
        total += snafu_dec(line.strip())

print(dec_snafu(total))