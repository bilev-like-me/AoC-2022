def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(int(n))
    p_dickt = {}
    for el in set(primfac):
        p_dickt[el] = primfac.count(el)
    return p_dickt

print(f'1500 = {primfacs(1500)}')
print(f'98 = {primfacs(98)}')
print(f'1598 = {primfacs(30)}')
