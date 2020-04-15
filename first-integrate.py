import math


def integrate(f, a, b, n):
    h = (b - a) / n
    sum = (f(a) + f(b)) * 0.5

    for i in range(1, n - 1):
        x = a + i * h
        sum = sum + f(x)
    return sum * h


def f1(x):
    return math.exp(-(x ** 2))


def f2(x):
    return math.sin(-(x ** 4))


# main program
n = 100
a = 0.0
b = 1.0
print("The approximation of f1 is: ", integrate(f1, a, b, n))
print("The approximation of f2 is: ", integrate(f2, a, b, n))
