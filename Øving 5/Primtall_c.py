from math import sqrt

def divisable(a, b):
    return a % b == 0

def isPrime(a):
    if a == 2 or a == 3: return True
    if a % 2 == 0: return False
    for i in range(5, round(sqrt(a) + 0.5), 2):
        if divisable(a, i):
            return 'False'
    return 'True'
