def prime_factors(n):
    pfs = []
    d = 2
    while n > 1:
        while n % d == 0:
            pfs.append(d)
            n /= d
        d += 1
        if d*d > n:
            if n > 1: pfs.append(n)
            break

    return pfs

print prime_factors(12)
