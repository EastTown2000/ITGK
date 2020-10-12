def altnum(n):
    """
    gir en liste(int) av funksjonen i oppgaven
    """
    a = []
    for i in range(1, n + 1):
        if i%2 == 0:
            s = - i**2
        else:
            s = i**2
        a.append(s)        
    return a

a = int(input('Hvilket tall i tall-serien vil du ha summen av: '))
print(sum(altnum(a)))