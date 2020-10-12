def divisable(a, b):
    return a % b == 0

def isPrime(a):
    for i in range(2, a):
        if divisable(a, i):
            return 'False'
    return 'True'
