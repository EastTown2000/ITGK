def gcd(a, b):
    while b != 0:
        gb = b
        b = a % b
        a = gb
    return a

def reduce_fraction(a, b):
    d = gcd(a, b)
    return (a/d, b/d)
