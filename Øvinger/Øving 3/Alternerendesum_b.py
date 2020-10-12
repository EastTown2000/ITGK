def altnum(k):
    """
    gir en liste(int) av funksjonen i oppgaven
    """
    a = []
    i = 1
    while sum(a) <= k:
        if i%2 == 0:
            s = - i**2
        else:
            s = i**2
        i += 1
        a.append(s)  
    return a[0:-1]

a = int(input('k = '))
print(f'Summen av tallene før summen blir større enn k er {sum(altnum(a))}. Antall iterasjoner: {len(altnum(a))}')
