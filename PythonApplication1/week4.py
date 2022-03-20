#task 1

def min4(a,b,c,d):
    return min([a,b,c,d])

print(min(*[int(input()) for i in range(4)]))

#task 2

def IsPointInSquare(x, y):
    return ('YES' if -1 <= x <= 1 and -1 <= y <= 1 else 'NO')


print(IsPointInSquare(*[float(input()) for i in range(2)]))

#task 3


def distance(x, y, xc, yc):
    return ((x - xc) ** 2 + (y - yc) ** 2) ** 0.5


def IsPointInCircle(x, y, xc, yc, r):
    return ('YES' if distance(x, y, xc, yc) <= r else 'NO')


print(IsPointInCircle(*[float(input()) for i in range(5)]))

#task 4 57/100


def eratosthenes(n):
    return [x for x in range(2, n + 1) if x not in [i for sub in
            [list(range(2 * j, n + 1, j)) for j in range(2, n // 2)]
            for i in sub]]

def MinDivisor(n):
    for i in eratosthenes(int(n**0.5)):
        if n % i == 0:
            return i
    return n

print(MinDivisor(int(input())))
 
#task 4 100/100


def MinDivisor(n):
    k = 2
    while n ** 0.5 >= k:
        if n % k == 0:
            return k
        else:
            k += 1
    return n


print(MinDivisor(int(input())))

#task 5


def IsPrime(n):
    k = 2
    while n ** 0.5 >= k:
        if n % k == 0:
            return print('NO')
        else:
            k += 1
    return print('YES')


print(IsPrime(int(input())))

#task 6


def power(a, n, b=1):
    if n == 1:
        return b*a
    if n >= 1:
        return power(a, n-1, b*a)
    return 1

print(power(float(input()), int(input())))

#task 7


def summa(a, b):
    if b > 0:
        return summa(a + 1, b - 1)

    return a

print(summa(int(input()), int(input())))

#task 8


def power(a, n):
    if a == 0:
        return a

    if n == 0:
        return 1

    if n % 2 == 0:
        return power(a * a, n / 2)

    return a * power(a * a, (n - 1) / 2)


print(power(float(input()), int(input())))

# task 9


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

#task 10


a = []
while True:
    i = int(input())
    a += [i]
    if i == 0:
        break

print(*sum(a))

#task 11


a = []
while True:
    i = int(input())
    a += [i]
    if i == 0:
        break

a = [print(_) for _ in  a[::-1]]
