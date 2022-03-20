

def eratosthenes(n):
    return [x for x in range(2, n + 1) if x not in [i for sub in
            [list(range(2 * j, n + 1, j)) for j in range(2, n // 2)]
            for i in sub]]


def MinDivisor(a, b):
    for i in eratosthenes(int(min(a, b))//2 + 1):
        while a % i == 0 and b % i == 0:
            a = a // i
            b = b // i
    return [a, b]


print(*MinDivisor(int(input()), int(input())))
