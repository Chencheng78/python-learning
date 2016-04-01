def checkio(n):
    fac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            fac.append(d)
            n //= d
        d += 1
    if n > 10:
        return 0
    elif n > 1:
       fac.append(n)
    print(fac)
    fac.sort(reverse=True)
    for i in range(1, len(fac)):
        a = fac.pop()
        b = fac.pop()
        if a * b < 10:
            fac.append(a*b)
        else:
            fac.append(b)
            fac.append(a)
            fac.sort(reverse=True)
    fac.sort(reverse=True)
    count = 0
    for i in range(0, len(fac)):
        count += fac[i] * pow(10,i)
    return count

print(checkio(12))
